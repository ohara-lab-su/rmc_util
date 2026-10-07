# rmc_util

RMC_POT の入力ファイルの作成・編集、構造データの変換、計算結果の読み取り・解析を行う Python ライブラリです。

RMC_POT の計算条件（`.dat`）、原子配置（`.cfg`）、構造制約（FNC・topology など）、計算結果（`.fit`・`.hst`・`.ppcf` など）を扱うためのモジュールを提供します。

## インストール

リポジトリのルートで実行します。

```bash
pip install .
```

## 主な機能

| 分野 | モジュール | 内容 |
| --- | --- | --- |
| RMC_POT | `rmc_pot` | RMC_POT 関連の操作 |
| 計算条件 | `rmc_pot_dat`、`rmc_pot_dat_fixed`、`rmc_pot_dat_free` | `.dat` の各書式 |
| 構造制約 | `rmc_pot_dat_fnc`、`rmc_pot_dat_top`、`rmc_pot_snc` | FNC、topology、SNC 関連 |
| 計算結果 | `rmc_pot_fit`、`rmc_pot_hst`、`rmc_pot_log`、`rmc_pot_ppcf` | フィット結果、履歴、ログ、部分二体分布関数 |
| データ変換 | `util` | CFG、POSCAR、GROMACS topology などの変換・補助処理 |

モジュールの公開クラス・メソッドは [API リファレンス](docs/api/index.md) を参照してください。

## ドキュメント

- [RMC 法と RMC_POT](docs/guide/overview.md)
- [入力ファイル](docs/guide/input.md)
- [構造制約](docs/guide/constraints.md)
- [出力と解析](docs/guide/output.md)
- [ファイル形式の詳説](docs/reference/index.md)
- [API リファレンス](docs/api/index.md)

ドキュメントをローカルで生成するには、`docs/build.sh` を実行します。HTML は `docs/_build/html/` に出力されます。

## 参考文献

Orsolya Gereben, *RMC_POT user guide for version 2023.1* (2023).
