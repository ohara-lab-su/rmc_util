# `rmc_util.util.find_next_log_index`

Source: `src/rmc_util/util/find_next_log_index.py`

## `next_log_dir_name(stage: str, log_index_width: Optional[int]=None)`

Determines the “next” log name from existing log directories (`log<integer>_(rmc|dft)`).

This helper manages log directory names uniquely with a single sequential number even when the numbers of RMC and DFT executions differ (for example, when RMC is run multiple times until convergence).

Purpose:
  - Scan existing "log<integer>_(rmc|dft)" names and find the maximum <integer>.
  - Use (maximum + 1) as the next number.
  - Append stage ("rmc" or "dft") as the suffix.

Number handling:
  - "log003_rmc" and "log3_rmc" are treated as the same integer 3 (zero padding only affects presentation).
  - If the maximum is 999, the next number is 1000 (the number of digits expands naturally).

Rules for zero-padding width (display format):
  - When log_index_width is None:
      Follow the maximum number of digits appearing in existing logs.
      However, expand naturally if the next number exceeds that width (e.g., 999→1000).
  - When log_index_width is an int:
      Zero-pad using that value as the base width.
      However, expand naturally if the next number exceeds that width.

Args:
    stage (str):
        Expected to be "rmc" or "dft". Used unchanged as the return-value suffix.
    log_index_width (Optional[int]):
        Base width for zero padding.
        If None, follow the width of existing logs.

Returns:
    str:
        Name of the next log directory to create.
        Examples: "log004_rmc", "log03_dft", "log1000_rmc"

Notes:
    - Only directory names directly under the current directory are scanned.
    - If no existing logs are present, the next number is 1.
    - This function does not validate stage (it does not reject values other than "rmc"/"dft").

## `find_next_log_index(prefix: str, max_loop: int)`

For RMC-DFT.

From existing prefixNN entries, returns:
  - The next index (next_index)
  - The number of digits (digits)

Examples:
  log0, log1, ... log9 → next log10 (digit width automatically increases from 1 to 2)
  log00, log01 → next log02
  log09 → next log10 (retains width 2)


## Methods


### Module function `next_log_dir_name()`

- Definition line: 11
- Description: Determines the “next” log name from existing log directories (`log<integer>_(rmc|dft)`).

### Module function `find_next_log_index()`

- Definition line: 94
- Description: For RMC-DFT.

## Argument and Return-Type List Based on Source Code

This section directly checks the function declarations and type annotations in the provided implementation. Arguments and return values without type annotations are marked “Not specified.” This does not mean that their runtime return value is `None`.

### `next_log_dir_name`

| Argument | Type annotation |
|---|---|
| `stage` | `str` |
| `log_index_width` | `Optional[int]` |

Return type annotation: `str`. Definition: `find_next_log_index.py:11`.

### `find_next_log_index`

| Argument | Type annotation |
|---|---|
| `prefix` | `str` |
| `max_loop` | `int` |

Return type annotation: `Tuple[int, int]`. Definition: `find_next_log_index.py:94`.
