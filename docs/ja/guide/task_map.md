# 利用目的から参照するマニュアル

このページは `README.ja.md` に記載された機能を、利用者の作業単位に整理した案内です。具体的な呼び出し例は [README のコード例](../tutorial/readme_examples.md)、メソッド名は [実装に基づく API 索引](../api/implementation_index.md)を参照してください。

| 目的 | 主なモジュール | 関連ページ |
| --- | --- | --- |
| 導入と編集用スクリプトの配置 | `install` | [インストール](installation.md) |
| RMC_POT の実行 | `RmcPot`、`runners.run_rmc` | [実行の流れ](../tutorial/workflow.md) |
| `.dat` の読み書きと形式の選択 | `RmcPotDat`、`RmcPotDatFixed`、`RmcPotDatFree` | [設定](../tutorial/configure.md) |
| FNC 制約の編集 | `RmcPotDatFnc` | [構造制約](../tutorial/constraints.md) |
| topology の編集 | `RmcPotDatTop` | [入力](input.md) |
| SNC / Qn 制約 | `RmcPotSnc` | [構造制約](../tutorial/constraints.md) |
| ログと収束履歴 | `RmcPotLog`、`RmcPotHst` | [結果解析](../tutorial/analysis.md) |
| フィットと部分二体分布関数 | `RmcPotFit`、`RmcPotPpcf` | [結果解析](../tutorial/analysis.md) |
| 構造形式変換 | `util.cfg2poscar`、`util.poscar2cfg` など | [API リファレンス](../api/index.md) |

## 利用上の区別

`rmc-util` は PyPI での配布名、`rmc_util` は Python の import 名です。`rmc_util install` が作業ディレクトリに配置する編集用スクリプトと、パッケージ内の実行処理は別です。配置済みスクリプトはパッケージ更新時に自動更新されません。詳しくは [README ベースのマニュアル](readme_manual.md) を参照してください。

RMC 法の理論と RMC_POT のファイル形式については、[RMC 法・RMC_POT の解説](../reference/index.md) に従来の解説を保持しています。
