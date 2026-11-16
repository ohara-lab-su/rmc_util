# 利用目的から参照するマニュアル

RMC_UTIL は RMC_POT の計算エンジンそのものではなく、入力ファイルの操作、計算実行の補助、出力データの読込み・解析を Python から扱うライブラリです。このページでは、実際の作業から対応するクラスと説明ページを探せるように整理します。RMC_POT の入力仕様は [入力ファイル](input.md)、計算結果の種類は [出力ファイル](output.md)、理論的背景は [RMC 法と RMC_POT](overview.md) を参照してください。

## 作業とモジュールの対応

| 作業 | 主なモジュール | 説明・API |
| --- | --- | --- |
| 編集用スクリプトの配置 | `install` | [導入 API](../api/install.md)、[利用マニュアル](readme_manual.md) |
| RMC_POT の実行 | `RmcPot`、`runners.run_rmc` | [RmcPot](../api/rmc_pot.md)、[実行処理](../api/runners_run_rmc.md) |
| `.dat` ファイルの読み書き | `RmcPotDat`、`RmcPotDatFixed`、`RmcPotDatFree` | [共通 API](../api/rmc_pot_dat.md)、[固定形式](../api/rmc_pot_dat_fixed.md)、[自由形式](../api/rmc_pot_dat_free.md) |
| FNC 制約の操作 | `RmcPotDatFnc` | [FNC API](../api/rmc_pot_dat_fnc.md)、[構造制約](constraints.md) |
| トポロジーファイルの操作 | `RmcPotDatTop` | [トポロジー API](../api/rmc_pot_dat_top.md)、[入力ファイル](input.md) |
| SNC 制約の操作 | `RmcPotSnc` | [SNC API](../api/rmc_pot_snc.md)、[構造制約](constraints.md) |
| 実行ログの読込み | `RmcPotLog` | [ログ API](../api/rmc_pot_log.md)、[出力ファイル](output.md) |
| 履歴ファイルの読込み | `RmcPotHst` | [履歴 API](../api/rmc_pot_hst.md)、[出力ファイル](output.md) |
| フィット結果の読込み | `RmcPotFit` | [フィット API](../api/rmc_pot_fit.md)、[出力ファイル](output.md) |
| 部分二体分布関数の読込み | `RmcPotPpcf` | [PPCF API](../api/rmc_pot_ppcf.md)、[出力ファイル](output.md) |
| 原子配置形式の変換 | `util.cfg2poscar`、`util.poscar2cfg` | [CFG→POSCAR](../api/util_cfg2poscar.md)、[POSCAR→CFG](../api/util_poscar2cfg.md) |

## 入力を準備する段階

最初に、原子配置 `*.cfg`、計算条件 `*.dat`、フィットに使用する実験データを揃えます。RMC_POT では `*.cfg` に記載した原子種の順序が部分相関の順序を決めるため、`*.dat` の部分ごとの cutoff や散乱係数と整合させる必要があります。固定形式と自由形式の `.dat` は記述規則が異なります。特に自由形式の `#002` と `#003` は X 線散乱係数の既定の取扱いが異なるため、単に先頭行を書き換えて同等とみなすことはできません。

分子の結合関係を保つ場合は FNC、トポロジーに基づく相互作用を扱う場合は `*.top` が関係します。これらは入力ファイルの役割が異なるため、制約とポテンシャルを同一のものとして扱わないでください。具体的な形式は [RMC_POT 入力ファイル詳説](../reference/rmcpot_input_explained.md) と [構造制約](constraints.md) に記載しています。

## 実行する段階

`RmcPot` と `runners.run_rmc` は実行側の機能を探す入口です。RMC_POT の反復では、原子の試行移動に対して実験データとの残差および指定された構造制約が評価されます。したがって、実行できたことと、目的の構造に収束したことは別に判断する必要があります。実行方法の具体的な引数や呼出し手順は、[RmcPot API](../api/rmc_pot.md) と [実行処理 API](../api/runners_run_rmc.md) を基準にしてください。

## 結果を確認する段階

実行後は、ログ、履歴、フィット結果、部分二体分布関数を目的に応じて使い分けます。ログは実行状態や評価値の確認、履歴は反復中の変化、フィット結果は計算値と実験値の比較、PPCF は原子種対ごとの局所構造の検討に用います。フィットの一致だけで構造の一意性が保証されるわけではないため、距離・配位数・結合角などの制約と併せて解釈してください。出力形式の詳細は [RMC_POT 出力ファイル詳説](../reference/rmcpot_output_explained.md) を参照してください。

## 配布名と実行環境の区別

`rmc-util` は配布パッケージ名、`rmc_util` は Python の import 名です。`rmc_util install` により作業ディレクトリへ配置される編集用スクリプトと、インストール済みパッケージ内の実装は区別します。既に配置したスクリプトはパッケージの更新だけでは自動更新されません。実際の運用手順は [利用マニュアル](readme_manual.md)、公開メソッドの一覧は [実装に基づく API 索引](../api/implementation_index.md) を参照してください。

*参照：RMC_POT user guide 2023.1, I.A、I.K–I.Q、II.C–II.I。RMC_UTIL の各機能の名称は既存の API ドキュメントに準拠します。*
