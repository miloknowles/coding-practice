from .heap import *

h = heap([4, 3, 2, 1], variant='min')
heapify(h)

# 1, 3, 2, 4
print(h)

heappush(h, 5)
print(h) # 1, 3, 2, 4, 5

heappush(h, 0) # 0, 1, 2, 3, 4, 5
print(h)

print(heappop(h)) # 0
print(heappop(h)) # 1

print(heappushpop(h, 13)) # 2
print(h)