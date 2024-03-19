from collections import OrderedDict, defaultdict


class LFUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    self.key_to_freq = {}
    self.freq_to_key = defaultdict(lambda: OrderedDict())
    self.lowest_freq = 1

  def _promote_key(self, key: int):
    if key not in self.key_to_freq:
      self.key_to_freq[key] = 1
      self.freq_to_key[1][key] = key
      self.lowest_freq = 1
    else:
      freq = self.key_to_freq[key]
      # Pop the key from its current frequency group.
      self.freq_to_key[freq].move_to_end(key)
      self.freq_to_key[freq].popitem(last=True)
      # The lowest frequency may be higher now!
      if len(self.freq_to_key[self.lowest_freq]) == 0:
        self.lowest_freq += 1
      self.key_to_freq[key] = freq + 1
      # Promote the key to the next frequency group.
      self.freq_to_key[freq + 1][key] = key

  def get(self, key: int) -> int:
    """Get the value of `key` from the cache."""
    if key not in self.cache:
      return -1
    else:
      self._promote_key(key)
      return self.cache[key]

  def put(self, key: int, value: int) -> None:
    """Add the key-value pair to the cache."""
    # If at capacity, need to remove the LRU and LFU item.
    if key not in self.cache and len(self.cache) >= self.capacity:
      # The last item added to the lowest frequency group will be the LFU and LRU.
      lfu_lru_key = self.freq_to_key[self.lowest_freq].popitem(last=False)[0]
      if len(self.freq_to_key[self.lowest_freq]) == 0:
        self.lowest_freq += 1
      del self.key_to_freq[lfu_lru_key]
      del self.cache[lfu_lru_key]

    # Now the cache is guaranteed to have space for one more entry.
    self._promote_key(key)
    self.cache[key] = value