from dataclasses import dataclass
from typing import Optional, Callable
from enum import Enum

from time import time, sleep

from concurrent.futures import ThreadPoolExecutor


class JobStatus(Enum):
  FULFILLED = "fulfilled"
  FAILED = "rejected"


@dataclass
class Job:
  func: Callable[..., any]
  args: tuple[any, ...] = ()
  kwargs: dict[str, any] = None

  def execute(self):
    self.func(*self.args, **(self.kwargs or {}))


@dataclass
class JobResult:
  result: any
  status: JobStatus
  reason: Exception


def execute_all(jobs: list[Job], max_workers: int = 4):
  with ThreadPoolExecutor(max_workers=max_workers) as pool:
    futures = [pool.submit(job.execute) for job in jobs]
    results = [f.result() for f in futures]
    return results
  

def simulate_io_bound_task():
  sleep(0.1)


J = 100
jobs = [
  Job(func=simulate_io_bound_task) for _ in range(J)
]


t0 = time()
execute_all(jobs, max_workers=10)
elapsed = time() - t0
print(f"elapsed: {elapsed:.3f}s")