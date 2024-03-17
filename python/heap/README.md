# Implement a (Min/Max) Heap using Python

It should support the following operations:
- `insert (heappush)` : Insert an item with `(key, value)` into the heap
- `find-max` : Return the item with maximum key
- `heapify` : Transform an unsorted list into a max heapify (same as heapsort)
- `update-key` : Change the key for an item (and re-heapify)
- `replace (heappushpop)` : Pop the root and insert a new item in a single operation. This avoids heapifying twice.
- `pop (heappop)` : Remove and return the maximum key item
- `nsmallest` : Return the n smallest items
- `nlargest` : Return the n largest items

The heap property: a node can only be a parent of nodes whose keys are lower than that of the parent. In an array, you can achieve this by storing the children of `i` at `2i+1` and `2i+2` in the array.