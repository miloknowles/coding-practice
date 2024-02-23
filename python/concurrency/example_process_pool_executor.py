import time
from concurrent.futures import ProcessPoolExecutor


def factorial(n: int) -> int:
  """An example of a CPU-intensive calculation."""
  assert(n >= 1)

  out = 1
  for i in range(2, n + 1):
    out *= i

  return out


def factorial_n2_times(n: int) -> int:
  """Even slower function. Just returns `n`."""
  for _ in range(n):
    for _ in range(n):
      factorial(n)
  return n


n = 128
n_jobs = 100
n_processes = 8


def serial_example():
  """Baseline: using a single CPU for calculations."""
  t0 = time.time()
  for _ in range(n_jobs):
    factorial_n2_times(n)
  print(f"elapsed (serial): {time.time() - t0:.3f}s")


def parallel_example():
  """Parallelized: using multiple CPUs for calculations."""
  t0 = time.time()
  with ProcessPoolExecutor(max_workers=n_processes) as pool:
    futures = [pool.submit(factorial_n2_times, n) for _ in range(n_jobs)]
    results = [f.result() for f in futures]
    print(results)
  print(f"elapsed (parallel): {time.time() - t0:.3f}s")


if __name__ == "__main__":
  serial_example()
  parallel_example()