import numpy as np

def longest_increasing(s: str | list) -> tuple[str | list, int]:
  """Find the longest increasing subsequence in `s`."""
  t = sorted(s)
  _, L = lcs(s, t)
  return backtrack(L, s, t)


def lcs_r(x: str, y: str) -> str:
  """Find the LCS recursively."""
  if len(x) == 0 or len(y) == 0:
    return ""

  # Match x and y at their first character.
  if x[0] == y[0]:
    return x[0] + lcs_r(x[1:], y[1:])

  else:
    # Option 1: Skip character x[0].
    lcs_suffix_skip_x = lcs_r(x[1:], y)

    # Option 2: Skip character y[0].
    lcs_suffix_skip_y = lcs_r(x, y[1:])

    return lcs_suffix_skip_x if len(lcs_suffix_skip_x) > len(lcs_suffix_skip_y) else lcs_suffix_skip_y


def lcs(x: str | list, y: str | list) -> tuple[int, np.ndarray]:
  """Find the longest common subsequence between `x` and `y`.
  
  Idea: If we know the LCS between x[:i] and y[:j], we can
  either extend it by matching x[i] and y[j], or we can
  skip x[i] or skip y[j].

  L[i, j]: "The LCS so far if we match x[i] to y[j]."
  """
  m, n = len(x), len(y)
  L = np.zeros((m + 1, n + 1))

  for i in range(1, m + 1):
    for j in range(1, n + 1):        
      # If we can match x[i] and y[j], extend the LCS of x[:i] and y[:j].
      if x[i - 1] == y[j - 1]:
        L[i, j] = L[i - 1, j - 1] + 1
      else:
        # Otherwise, the LCS could be achieved by either skipping x[i] or skipping x[j].
        L[i, j] = max(L[i - 1, j], L[i, j - 1])

  return L[m, n], L


def backtrack(L: np.ndarray, x: str | list, y: str | list) -> str | list:
  """Trace the LCS of two strings `x` and `y`."""
  out = ""

  i, j = len(x), len(y)
  while i > 0 and j > 0:
    if x[i - 1] == y[j - 1]:
      out += x[i - 1]
      i -= 1
      j -= 1
    else:
      if L[i-1, j] >= L[i, j-1]:
        i -= 1
      else:
        j -= 1

  return "".join(list(reversed(out)))


if __name__ == "__main__":
  x = "abcdef"
  y = "a_b_cdef"
  length, L = lcs(x, y)
  print(length, "\n", L)

  print(backtrack(L, x, y))

  longest_increasing("abaaaac")