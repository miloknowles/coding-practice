import numpy as np
import math
from itertools import accumulate


def sort_by_digit(x: list[int], d: int, base: int = 10) -> list[int]:
  """Sort a list of integers `x` by the the `dth` digit.

  Note that `d=0` represents the least-significant digit.
  """
  # How many times does each value of the digit occur?
  digit_value_counts = [0 for _ in range(base)]

  for full_value in x:
    # Shift the value right `d` times, and then take the value in the
    # ones position.
    digit_value_counts[full_value // base**d % base] += 1

  # Transform the value counts into cumulative counts.
  # Note that the value at index d will be the LAST index at which a list
  # item with this digit value should be inserted into the output list.
  next_insert_index_for_value = list(accumulate(digit_value_counts))

  out = [0 for _ in range(len(x))]

  # Insert each item in `x` into its sorted position in the output.
  for full_value in reversed(x):
    digit_value = full_value // base**d % base
    next_insert_index_for_value[digit_value] -= 1
    insert_at_idx = next_insert_index_for_value[digit_value]
    out[insert_at_idx] = full_value

  return out


def radix_sort(x: list[int], base: int = 10) -> list:
  """Implements radix sort for integer arrays."""
  max_digit = int(math.log(max(x), base))

  for d in range(0, max_digit + 1):
    x = sort_by_digit(x, d, base)

  return x