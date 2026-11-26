# RMC_Util 開発引継書

更新日 2026-11-27。開発時の継続ルールは [AGENTS.md](AGENTS.md) に記載する。

## 分離の経緯と現在地

RMC_Util は、RMC_POT の入力準備・実行・結果解析を担う Python パッケージ。計算そのものは外部の RMC_POT 実行ファイルが行う。単独の RMC 計算と、`rmc_dft` が RMC と VASP を交互に実行するときの両方で使われる。

| 対象 | 照合した版 | 分離後の責務 |
| --- | --- | --- |
| `rmc_util` | 現作業ツリーの `pyproject.toml` は 0.1.12。ローカル HEAD は `11568ce`、最新ローカルタグは `v0.1.11` | RMC_POT の入力・実行・解析と CFG 側の変換 |
| 添付 `rmc_dft.zip` | アーカイブ内の `pyproject.toml` は 0.7.15 | 両ライブラリを使った連成実行、構造の受け渡し、再開、手動順序、番号付き init |
| 添付 `vasp_util.zip` | アーカイブ内の `pyproject.toml` は 0.0.9。README と変更履歴の runner の説明は主に v0.0.8 | VASP 入力・起動・出力処理。VASP 側の計算条件は `vasp_init.py` で編集 |

- RMC 機能の分離元は `rmc_dft` v0.6.13。現リポジトリの [CHANGELOG.ja.md](CHANGELOG.ja.md) v0.0.0 と添付 `rmc_dft/CHANGELOG.ja.md` v0.7.0 が対応する。VASP の分離元は添付 `vasp_util/README.ja.md` の記載では RMC-DFT 0.7.10。
- 添付 `rmc_dft` は `rmc-util` と `vasp-util` に依存し、添付 `vasp_util` は `rmc-util` に依存する。現行 RMC_Util の配布依存にこの二つは含まれない。v0.1.10 の循環 import 修正では `RmcPotLog` の `Config` を `rmc_util.config` に戻した。現行パッケージの公開名は [__init__.py](src/rmc_util/__init__.py) で明示的に import している。
- 添付 `rmc_dft/src/rmc_dft/__init__.py` と `rmc_pot/__init__.py` は一部の旧 import を再公開する。後者のサブモジュール別名を `sys.modules` に登録するループはコメントアウトされている。移行時は旧 import の経路ごとに可否を確認する。
- v0.1.0 で固定・自由形式の入力対応を拡張し、v0.1.5 で CLI を `rmc_util install` に整理。v0.1.6 以降に起動ファイルと runner の分離を進め、v0.1.11 で `config.yml` を同梱。v0.1.12 の作業差分は plot 4本と CLI の一覧・個別配置を追加している。v0.1.6 の履歴には「起動ファイルを配布」と「init のみを配布」の記載が併存する。各版の配布内容を説明する際は該当版の設定を確認する。

## 入口から結果まで

1. **配布と作業ディレクトリ** — [pyproject.toml](pyproject.toml) の console entry point は `rmc_util.install:main`。配布ファイルの配置元は `share/rmc_util/scripts`。[install.py](src/rmc_util/install.py) はインストール先と配布物の記録から探索し、同名を重複させず名前順で扱う。現作業ツリーの `install`、`install all`、`install script` は一括配置、`install <名前>` は1件、`list` は名前と用途を列表示する。`.py`、`.yml` は個別指定時に省略できる。通常は同名ファイルをスキップし、`--force` で上書きする。POSIX では `rmc.py` に実行権限を付ける。
2. **単独 RMC の起動** — [rmc.py](scripts/rmc.py) がカレントディレクトリの `config.yml` を [Config](src/rmc_util/config.py) で読み、`RmcPotLog` と `RmcPotDat` を生成する。[rmc_init.py](scripts/rmc_init.py) の `run_rmc_init()` で計算条件を適用し、[run_rmc()](src/rmc_util/runners/run_rmc.py) に渡す。`Config` はインスタンスの YAML 読込とクラス側の `load_yaml()` を持つ。設定の更新範囲を変える場合は両経路を見る。
3. **入力と制約** — [RmcPotDat](src/rmc_util/rmc_pot_dat.py) は固定・自由形式の共通窓口。`init(prefer_existing=True)` は既存の `.dat` を優先し、先頭の `#002`・`#003` を自由形式として識別する。新規なら `use_free_format` を使い、`prefer_existing=False` で既存を再作成する際は `.bak_init` に退避する。固定形式は物理行、自由形式はセクションとキーが基準。FNC、topology、SNC はそれぞれ `rmc_pot_dat_fnc.py`、`rmc_pot_dat_top.py`、`rmc_pot_snc.py` を参照する。
4. **RMC の実行・後処理** — `run_rmc()` は呼び出し側から `config` と `rmc_dat` を受け取る。`RmcPot` の入力検査、FNC と cutoff の整合確認、外部実行を順に呼ぶ。後処理有効時は `finally` で結果整理・バックアップ・`<cfg_name>.vasp` への変換を行う。収束の判定と反復は `auto_converge` を指定した場合に行う。[RmcPot](src/rmc_util/rmc_pot.py) の前処理には既存 CFG が必要。初期構造を変換する場合は明示的に [変換ユーティリティ](src/rmc_util/util/) を呼ぶ。
5. **統合 RMC–DFT** — 添付 `rmc_dft` の通常 runner と sequence runner は `rmc_util.runners.run_rmc` と `vasp_util.runners.run_vasp` を呼び出す。通常は RMC 後の `<cfg_name>.vasp` を `POSCAR` に渡し、VASP 後の CFG を次の RMC に使う。通常 init は `rmc_init.py` と `rmc_vasp_init.py`。番号付き init と `CONTINUE_NUMBERED_INIT`、`restart`、手動シーケンスの処理は統合側を確認する。`RmcDft` クラスにも交互実行の API があるため、runner との呼び分けに注意する。
6. **結果の読取と作図** — `RmcPotLog` は実行ログと結果の収集、`RmcPotHst` は反復履歴と収束、`RmcPotFit` はフィット、`RmcPotPpcf` は部分二体分布を担当する。`plot_fit.py` は計算と実験の S(Q)、`plot_hst.py` は χ² の推移、`plot_ppcf.py` は原子種ペアの重ね描き、`plot_ppcf2.py` はペアごとのパネル表示。現作業ツリーの plot は読取クラスを `rmc_util` から import し、Matplotlib で描画する。

仕様調査は [日英 README の日本語版](README.ja.md)、[Pages の作業別案内](docs/ja/guide/task_map.md)、[入力・出力の詳説](docs/ja/reference/index.md)、[API](docs/ja/api/index.md) から始め、対象ファイルと実装に戻って確認する。統合側の移行経緯は添付 `rmc_dft/README.ja.md` と `CHANGELOG.ja.md`、VASP 単独実行は添付 `vasp_util/README.ja.md` と `CHANGELOG.ja.md` が入口。

## 検証状況と次に確認すること

| 項目 | 確認済みと残り |
| --- | --- |
| v0.1.11 の配布 | 過去のローカル検証で wheel と sdist の3ファイル収録、wheel を入れた仮想環境で YAML の配置・読込・上書き制御を確認済み。日英 Pages の HTML 生成も確認済み。当時の検証結果であり、現作業ツリーの v0.1.12 には引き継がない。 |
| v0.1.12 の配布 | 前回の模擬検証で7ファイルの一覧・列揃え、全指定、拡張子あり・なしの個別指定、スキップと上書きを確認。次は実際の wheel/sdist 内容、隔離した環境での CLI、実データでの plot 4本、日英 HTML を確認する。 |
| 単独起動時の依存 | 現行 `rmc.py` は RMC 側 `Config` を生成するが、`rmc_init.py` は冒頭で `vasp_util` から型注釈の `Config` と未使用の VASP クラスを import する。`vasp-util` は RMC_Util の配布依存にない。単体の新規環境で起動結果を確認し、整理時は統合側の init 互換性も見る。 |
| ログと再開 | [next_log_dir_name()](src/rmc_util/util/find_next_log_index.py) は既存の `log<番号>_rmc`・`log<番号>_dft` の両方を走査し、最大の次を採番する。空のディレクトリでは実装上は 0 始まりで、同関数 docstring の「1」と不一致。統合側の再開判定を照合してから説明や仕様を変更する。 |
| 統合と障害時 | 添付三者の組合せで、通常・手動シーケンス、既存ログからの再開、番号付き init、Ctrl+C や実行失敗時の結果退避は未実行。添付 VASP runner は処理失敗時に `sys.exit(-1)` を呼び、RMC runner の `False` 返却とは扱いが異なる。呼び出し側を含めて確認する。 |
| 公開 | [Pages workflow](.github/workflows/pages.yml) は main への push または手動起動で [docs/build.sh](docs/build.sh) を実行し、Sphinx の英語出力を公開ルートにも配置する。[PyPI workflow](.github/workflows/publish-pypi.yml) は GitHub Release の公開または手動起動で配布物をビルド・公開する。今回はローカル設定の確認まで。リモートの公開状況は未確認。 |

今回の作業は参照資料の照合とこの引継書・開発規約の追加。既存の v0.1.12 の作業差分とステージ状態は引き継ぐ。今後は作業ごとに、確認した版、設計上の判断、試した入口と結果、残る確認をこの文書で更新する。
