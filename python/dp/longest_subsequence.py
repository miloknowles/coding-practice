import numpy as np


def lcs_r(a: str, b: str) -> int:
  """Find the longest common subsequence between `a` and `b`."""
  if len(a) == 0 or len(b) == 0:
    return 0

  if a[0] == b[0]:
    return 1 + lcs_r(a[1:], b[1:])

  else:
    return max(
      lcs_r(a[1:], b),
      lcs_r(a, b[1:])
    )


def lcs_b(a: str, b: str) -> int:
  """Find the longest common subsequence using bottom-up DP."""
  dp = np.zeros((len(a), len(b)))

  for i in range(len(a)):
    for j in range(len(b)):
      if a[i] == b[j]:
        before = dp[i-1, j-1] if (i >= 1 and j >= 1) else 0
        dp[i, j] = before + 1
      else:
        dp[i, j] = max(dp[i-1, j], dp[i, j-1])

  return dp[len(a) - 1, len(b) - 1]