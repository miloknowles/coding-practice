import time

from threading import Thread
from queue import Queue


def io_heavy_task(n: int):
  """Simulates an IO operation, like waiting for an API."""
  time.sleep(0.1)


def task_worker(q: Queue):
  while not q.empty():
    n = q.get()
    io_heavy_task(n)
    q.task_done()


n_tasks = 10
n_threads = 10
n = 50


# Do the work with a single thread:
t0 = time.time()
print("Running synchronously:")
r = []
for _ in range(n_tasks):
  r.append(io_heavy_task(n))
print(f"elapsed: {time.time() - t0:.5f}")


# Try doing the work with many threads:
# This will help because the scheduler can suspend threads as needed (e.g after 15ms).
# It will see if a thread is IO blocked and do another task if so. This allows
# all of the threads to start their waiting immediately, and 
t0 = time.time()
print(f"Running asynchronously with {n_threads} threads:")
r = []

q = Queue()
for _ in range(n_tasks):
  q.put(n)

for _ in range(n_threads):
  t = Thread(target=task_worker, args=(q,))
  t.start()

q.join()

print(f"elapsed: {time.time() - t0:.5f}")