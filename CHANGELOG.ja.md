# 変更履歴

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/CHANGELOG.md)
[![ja](https://img.shields.io/badge/lang-ja-yellow.svg)](https://github.com/ohara-lab-su/rmc_util/blob/main/CHANGELOG.ja.md)

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
