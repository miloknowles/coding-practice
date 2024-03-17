def merge_sort(l: list[any]):
  # Base case: if l is trivially sorted, return it.
  if len(l) <= 1:
    return l

  m = len(l) // 2 # middle index
  left, right = l[:m], l[m:]

  # Sort left and right.
  _left = merge_sort(left)
  _right = merge_sort(right)

  # Then merge the sorted results.
  merged = merge(_left, _right)

  return merged


def merge(l1: list[any], l2: list[any]) -> list[any]:
  """Merges two sorted lists l1 and l2."""
  out = []
  i, j = 0, 0
  while i < len(l1) and j < len(l2):
    if l1[i] <= l2[j]:
      out.append(l1[i])
      i += 1
    else:
      out.append(l2[j])
      j += 1

  # At this point, one of the lists may have remaining elements.
  if i < len(l1):
    out.extend(l1[i:])
  elif j < len(l2):
    out.extend(l2[j:])


merge_sort([1, 3, 2, 4, 5, 2])