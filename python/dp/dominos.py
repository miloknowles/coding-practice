import random


def find_longest_sequence(start, remaining):
  """
  Return the longest sequence that can be made from remaining dominos (set of tup).
  """
  # Base case: none remaining, return zero.
  if len(remaining) == 0:
    return 0, []

  # Try every possible remaining domino (both direction) and return the longest subsequence that can
  # be made from them.
  best_length = 0
  best_seq = None

  for d in remaining:
    length_using = 0
    seq_using = None

    remaining_without = remaining.copy()
    remaining_without.remove(d)

    if d[0] == start[1]:
      length_using, seq_using = find_longest_sequence((d[0], d[1]), remaining_without)
    elif d[1] == start[1]:
      length_using, seq_using = find_longest_sequence((d[1], d[0]), remaining_without)

    if length_using > best_length:
      best_length = length_using
      best_seq = seq_using

  # Some logic to avoid concatenate None to a list.
  return 1 + best_length, [start] + best_seq if best_seq is not None else [start]


def find_longest_sequence_multistart(start_value, domino_tup):
  """
  Try out multiple starting dominos and return optimized sequence.
  """
  best_length = 0
  best_seq = None

  # Add possible start dominos in correct orientation.
  start_set = set()
  for d in domino_tup:
    if d[0] == start_value or d[1] == start_value:
      start_set.add(d if d[0] == start_value else (d[1], d[0]))

  # Try each starting domino.
  for s in start_set:
    remaining =  domino_tup.copy()

    if s in remaining:
      remaining.remove(s)
    else:
      remaining.remove((s[1], s[0]))

    l, s = find_longest_sequence(s, remaining)
    if l > best_length:
      best_length = l
      best_seq = s

  return best_length, best_seq


if __name__ == "__main__":
  start_value = 5
  domino_tup = set([
    (5, 0), (0, 10), (10, 9), (9, 7), (7, 8), (9, 1), (1, 3), (3, 5), (4, 2), (12, 2), (2, 1), (5, 6)
  ])

  l, s = find_longest_sequence_multistart(start_value, domino_tup)
  print("\n==> Optimized sequence:")
  print("==> Length = {}".format(l))
  print("==> Sequence =", s)
