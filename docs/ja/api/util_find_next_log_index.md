# `rmc_util.util.find_next_log_index`

ソース: `src/rmc_util/util/find_next_log_index.py`

## `next_log_dir_name(stage: str, log_index_width: Optional[int]=None)`

既存のログディレクトリ（log<整数>_(rmc|dft)）から「次に使う」ログ名を決める。

本関数は、RMC と DFT の実行回数が一致しない（RMC を収束まで複数回回す）状況でも、
ログディレクトリ名を単一の通し番号で一意に管理するための補助である。

目的：
  - 既存の "log<整数>_(rmc|dft)" を走査し、最大の <整数> を見つける
  - 次番号として (最大値 + 1) を採用する
  - suffix として stage（"rmc" または "dft"）を付与する

番号の扱い：
  - "log003_rmc" と "log3_rmc" は同じ整数 3 として扱う（ゼロ埋めは表示上の問題）
  - 最大が 999 の場合、次は 1000 とする（桁あふれは自然に桁拡張）

ゼロ埋め幅（表示形式）の規則：
  - log_index_width が None の場合：
      既存ログに現れる数字部の最大桁数に追従する。
      ただし次番号がそれを超える場合（例：999→1000）は自然に桁拡張する。
  - log_index_width が int の場合：
      その値を「基本幅」としてゼロ埋めする。
      ただし次番号がその幅を超える場合は自然に桁拡張する。

Args:
    stage (str):
        "rmc" または "dft" を想定する。戻り値の suffix にそのまま使う。
    log_index_width (Optional[int]):
        ゼロ埋め幅の基本値。
        None の場合は既存ログ幅に追従する。

Returns:
    str:
        次に作成するログディレクトリ名。
        例： "log004_rmc", "log03_dft", "log1000_rmc"

Notes:
    - 走査対象はカレントディレクトリ直下のディレクトリ名のみ。
    - 既存ログが存在しない場合、次番号は 1 とする。
    - stage 自体の妥当性チェック（"rmc"/"dft" 以外の拒否）はここでは行わない。

## `find_next_log_index(prefix: str, max_loop: int)`

RMC-DFT 用

既存 prefixNN から
  - 次に使うインデックス(next_index)
  - 桁数(digits)
を返す。

例:
  log0, log1, ... log9 → 次 log10（桁は1→2へ自動昇格）
  log00, log01 → 次 log02
  log09 → 次 log10（桁は2を維持）


## 実装に基づく API 一覧


### モジュール関数 `next_log_dir_name()`

- 定義位置：11 行
- 説明：既存のログディレクトリ（log<整数>_(rmc|dft)）から「次に使う」ログ名を決める。

### モジュール関数 `find_next_log_index()`

- 定義位置：94 行
- 説明：RMC-DFT 用

## ソースコードに基づく引数・戻り値一覧


### `next_log_dir_name`

| 引数 | 型注釈 |
|---|---|
| `stage` | `str` |
| `log_index_width` | `Optional[int]` |

戻り値の型注釈: `str`。定義位置: `find_next_log_index(20261116-081327).py:11`。

### `find_next_log_index`

| 引数 | 型注釈 |
|---|---|
| `prefix` | `str` |
| `max_loop` | `int` |

戻り値の型注釈: `Tuple[int, int]`。定義位置: `find_next_log_index(20261116-081327).py:94`。

