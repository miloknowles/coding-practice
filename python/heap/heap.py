class heap(list):
  def __init__(self, other: list = [], variant: str = 'min'):
    """Initialize the heap from a `list` of values."""
    super(heap, self).__init__(other)
    if variant not in ('min', 'max'):
      raise ValueError("The heap variant must be either 'min' or 'max'.")
    self.variant = variant


class minheap(heap):
  def __init__(self, other: list = []):
    super(minheap, self).__init__(other, 'min')


class maxheap(heap):
  def __init__(self, other: list = []):
    super(maxheap, self).__init__(other, 'max')


def argsup(a, b, c1, c2, variant: str):
  if superior(a, b, variant):
    return c1
  else:
    return c2


def superior(a, b, variant: str):
  if a is None:
    return b
  elif b is None:
    return a
  else:
    return a >= b if variant == 'max' else a <= b


def inferior(a, b, variant: str):
  if a is None:
    return b
  elif b is None:
    return a
  return a < b if variant == 'max' else a > b


def swap(l, i1, i2):
  l[i1], l[i2] = l[i2], l[i1]


c1 = lambda i: 2*i + 1
c2 = lambda i: 2*i + 2
p = lambda i: (i - 1) // 2


def siftdown(h: list, i: int, variant: str):
  """Move item at index `i` down until the heap property is restored."""
  while (
    (c1(i) < len(h) and inferior(h[i], h[c1(i)], variant)) or \
    (c2(i) < len(h) and inferior(h[i], h[c2(i)], variant))
  ):
    # Swap the parent with the superior of the two children.
    sup_of_c1_or_c2 = argsup(h[c1(i)] if c1(i) < len(h) else None, h[c2(i)] if c2(i) < len(h) else None, c1(i), c2(i), variant)
    swap(h, i, sup_of_c1_or_c2)
    i = sup_of_c1_or_c2


def siftup(h: list, i: int, variant: str):
  """Move the item at index `i` up until the heap property is restored."""
  if i < 0:
    i = len(h) + i
  while i > 0 and superior(h[i], h[p(i)], variant):
    # Swap the child with its parent.
    swap(h, i, p(i))
    i = p(i)


def heapify(h: heap):
  """Transform heap with possible violations into a valid heap, in place."""
  # For each item, sift DOWN until the heap property is satisfied.
  # To do this, swap the item at `i` with children repeatedly.
  for i in reversed(range(len(h) - 1)):
    siftdown(h, i, h.variant)


def heappush(h: heap, item: any):
  """Insert an item into the heap, maintaining the heap property."""
  h.append(item)
  siftup(h, -1, h.variant)


def heappop(h: heap) -> any:
  """Removes and returns the supreme item."""
  swap(h, 0, -1)
  item = h.pop()
  siftdown(h, 0, h.variant)
  return item


def heappushpop(h: heap, item: any) -> any:
  """Push a new item to the heap and then pop the supremum."""
  h.append(item)
  swap(h, 0, -1)
  sup = h.pop()
  siftdown(h, 0, h.variant)
  return sup