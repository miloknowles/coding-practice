import time

from threading import Thread
from queue import Queue


def cpu_heavy_task(n: int):
  """Simulates some CPU-intensive work."""
  c = 0
  for _ in range(n):
    for _ in range(n):
      for _ in range(n):
        for _ in range(n):
          c += 1
  return c


def task_worker(q: Queue):
  """Worker that gets a task from the queue and does it."""
  while not q.empty():
    n = q.get()
    cpu_heavy_task(n)
    q.task_done()


n_tasks = 10
n_threads = 8
n = 50


# Do the work with a single thread:
t0 = time.time()
print("--- Running synchronously:")
r = []
for _ in range(n_tasks):
  r.append(cpu_heavy_task(n))
print(r)
print(f"elapsed: {time.time() - t0:.5f}")


# Try doing the work with many threads:
# This WILL NOT help things run any faster, since the task is CPU bound, and the
# same amount of CPU resources are available between all of the threads.
t0 = time.time()

print(f"--- Running asynchronously with {n_threads} threads:")
r = []

q = Queue()
for _ in range(n_tasks):
  q.put(n)

for _ in range(n_threads):
  t = Thread(target=task_worker, args=(q,))
  t.start()

q.join()

print(f"elapsed: {time.time() - t0:.5f}")