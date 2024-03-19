def lps_td(s: str, i: int, j: int, memo: dict) -> str:
  """Find the longest palindromic subsequence between `i` and `j` inclusive using top-down DP."""
  if j < i:
    return ""
  elif i == j:
    return s[i]
  elif (s, i, j) in memo:
    return memo[(s, i, j)]
  # Add s[i] and s[i] to the front and end of the palindrome.
  elif s[i] == s[j]:
    return s[i] + lps_td(s, i + 1, j - 1, memo) + s[j]
  else:
    skip_i: str = lps_td(s, i + 1, j, memo)
    skip_j: str = lps_td(s, i, j - 1, memo)
    best: str = skip_i if len(skip_i) >= len(skip_j) else skip_j
    memo[(s, i, j)] = best
    return best


def lps_bu(s: str) -> int:
  """Find the longest palindromic subsequence using bottom-up DP."""
  n = len(s)
  L = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n - 1, -1, -1):
    for j in range(i, n):
      if i == j:
        L[i][j] = 1
      elif s[i] == s[j]:
        L[i][j] = 2 + L[i + 1][j - 1]
      else:
        L[i][j] = max(L[i + 1][j], L[i][j - 1])
  return L[0][-1]


if __name__ == "__main__":
  memo = {}
  s = "amanaplanacanalpanama"
  longest = lps_td(s, 0, len(s) - 1, memo)
  print(longest)