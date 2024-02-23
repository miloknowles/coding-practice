import time
import asyncio

_n_tasks = 20
_sleep_time_sec = 0.1


# -------------------------------------------
def expensive_api_call(i: int):
  """Simulates an API call that has to wait a while."""
  time.sleep(_sleep_time_sec)
  return i, "ok"


async def expensive_api_call_async(i: int):
  """Simulates an API call that has to wait a while."""
  # Note that Python's `sleep` is blocking!
  # We have to use `asyncio.sleep` to simulate a non-blocking API call. It
  # allows the scheduler to do other tasks while it's waiting.
  await asyncio.sleep(_sleep_time_sec)
  return i, "ok"


# -------------------------------------------
def worker(i: int):
  code, r = expensive_api_call(i)
  return code, r


async def worker_async(i: int):
  code, r = await expensive_api_call_async(i)
  return code, r


# -------------------------------------------
def main_sync():
  """Do tasks serially. Wait for each worker to finish before the next runs."""
  t0 = time.time()

  results = []
  for i in range(_n_tasks):
    results.append(worker(i))

  elapsed = time.time() - t0
  print(f"sync took {elapsed:.5f} sec")
  print(results)


# -------------------------------------------
async def main_async_await():
  """Do async tasks, but await each one. This is the same as running serially."""
  t0 = time.time()

  results = []
  for i in range(_n_tasks):
    results.append(await worker_async(i))

  elapsed = time.time() - t0
  print(f"async/await took {elapsed:.5f} sec")
  print(results)


async def main_async_nonblocking():
  """Do async tasks, but don't await each one."""
  t0 = time.time()

  # This is a way to await the aggregate of many results.
  results = await asyncio.gather(*[worker_async(i) for i in range(_n_tasks)])
  
  elapsed = time.time() - t0
  print(f"async took {elapsed:.5f} sec")
  print(results)


if __name__ == "__main__":
  # This runs all the tasks in a sequential, blocking way:
  main_sync() # about 3.1 sec

  # This is a misuse of async/await, since we still await each result in order:
  asyncio.run(main_async_await()) # about 3.1 sec

  # This is the correct use of async/await, since we let asyncio gather all the
  # results without waiting on one at a time:
  asyncio.run(main_async_nonblocking())