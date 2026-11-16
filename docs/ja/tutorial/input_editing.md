# RMC_POT 入力ファイルの編集

`RmcPotDat` は、固定形式と自由形式の `.dat` ファイルに共通の Python インターフェースを提供します。両形式に共通するパラメーターは同じ setter で設定し、出力形式は初期化時に選択します。

```python
from rmc_util import RmcPotDat

rmc_dat = RmcPotDat(cfg_name="sample", auto_write=False)
rmc_dat.init(use_free_format=True, prefer_existing=True)
rmc_dat.set_density(0.0665715652)
rmc_dat.set_cutoffs([2.40, 1.25, 2.10])
rmc_dat.set_maximum_moves([0.01, 0.01])
rmc_dat.write()
```

新規の固定形式ファイルを作成する場合は `use_free_format=False` を指定します。`prefer_existing=True` で既存の `.dat` ファイルがある場合、`use_free_format` の指定よりも既存ファイルの形式判定が優先されます。初期化方法を選ぶ前に既存ファイルを確認してください。

形式別の処理は `rmc_pot_dat_fixed` と `rmc_pot_dat_free` に分かれていますが、通常の入力編集には共通の `RmcPotDat` インターフェースを使用します。FNC とトポロジーの設定には対応する補助モジュールを使用します。配位数や SNC 制約などの自由形式セクションは自由形式の機能を必要とし、固定形式のテキストレコードと互換ではありません。

原子種数の異なる設定例や構造制約の例は [計算条件](configure.md) と [構造制約](constraints.md) を参照してください。Python インターフェースは [API リファレンス](../api/rmc_pot_dat.md)、ファイル仕様は [RMC_POT 入力形式](../reference/rmcpot_input_explained.md) に記載しています。
