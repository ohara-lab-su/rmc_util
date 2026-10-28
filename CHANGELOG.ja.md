# 変更履歴

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/CHANGELOG.md)
[![ja](https://img.shields.io/badge/lang-ja-yellow.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/CHANGELOG.ja.md)


## v0.1.5

- `install_scripts.py` を `install.py` に変更し、CLI コマンドを `rmc_util-install` から `rmc_util` に変更した。
- `rmc_util install` で、編集用サンプルスクリプトをカレントディレクトリへコピーできるようにした。
- `rmc_util install --force` で既存ファイルを上書きできるようにした。`--force` を指定しない場合は既存ファイルをスキップする。
- 既存のスクリプト探索・コピー処理は維持した。

使用方法：

```bash
rmc_util install
rmc_util install --force
```

## v0.1.4

- rmc_util-install 対応
  サンプルスクリプトをカレントディレクトリにインストールする

## v0.1.0

### DAT free/fixed 対応拡張

RMC_POT マニュアルおよび規格サンプルに合わせ、`.dat` の free format / fixed format の取扱いを拡張した。
既存の実装方式を維持し、free format はセクション・キー構造、fixed format は物理行を基準として処理する。

### Free format

- `[ NBPOT ]` の Lennard-Jones 非結合ポテンシャル設定の読込・設定に対応した。
- `[ CUSTMOVE ]` の `NMOVED-ATOMS` および複数の `CUSTOM-LINE` の読込・設定に対応した。
- `[ LOCINV ]` の local invariance 設定に対応した。
    - `LOC-MODE`
    - `LOC-R-SPACING`
    - `LOC-INT-FROM_SIGMA`
    - `LOC-INT-FROM_SIGMA-MASTER`
    - `LOC-INT-FROM_SIGMA-SCALABLE`
    - `LOC-INT-TO`
- `[ NOPER ]` の非周期境界条件に対応した。
    - `SAMPLE-RADIUS`
    - `RECENTRE-SPHERE`
- `[ VIBRAMP ]` の `GAUSSIAN-SIGMA` の読込・設定に対応した。
- advanced geometric constraint の `[ CONC ]` の読込・設定に対応した。
- 既存の free-format セクション・キー処理を利用し、新しい汎用パーサや不要な抽象化は追加していない。

### Fixed format

- fixed format の既存の物理行ベースの処理方式を維持した。
- `_LOCAL_INV` 有効時の local invariance 行の読込・設定に対応した。
- `_NO_PERIODIC` 有効時の spherical sample 設定の読込・設定に対応した。
- `_VIBR_AMP` 有効時の vibrational amplitude の読込・設定に対応した。
- optional な fixed-format 行を既存方式のまま操作できるよう、指定した物理行への挿入・削除処理を追加した。
- fixed format の位置判定にはコメントを使用しない。コメント文字列の内容や表記には依存しない。
- UTF-8 で読めない既存 fixed-format ファイルに対して CP1252 読込のフォールバックを追加した。

### 対象

Ar potential、CCl4 atomic/molecular、local invariance、flexible molecule、non-periodic、vibrational amplitude、advanced
geometric constraint など、RMC_POT マニュアルおよび規格サンプルで使用される `.dat` 設定を扱うための拡張である。

## v0.0.5 - 2026-10-12

- README を更新し、インストール方法と現在の `rmc_util` の機能・利用方法の説明を改善。
- RMC_POT の fixed / free format を `RmcPotDat` の共通 API から扱えることを説明に追加。
- RMC-DFT などの上位ワークフローから RMC_POT をハンドリングする利用例を追加。

## v0.0.3

- LICENSE の追加

## v0.0.2 - 2026-10-07

- bugfix (モジュール周り)

## v0.0.1 - 2026-10-07

- RMC_DFT からの分離による import 調整

## v0.0.0 — 2026-10-07

### 初期リリース

- `rmc_dft` v0.6.13 から RMC 関連機能を分離し、`rmc_util` として独立した Python パッケージを作成。
- RMC_POT の入力データ・設定ファイルおよび出力データを扱うモジュールを収録。
- RMC_POT 関連のファイル変換・解析ユーティリティを収録。
- RMC 用 README とドキュメントを整備。

**由来:** 本バージョンの分離元は `rmc_dft` **v0.6.13**。
