import time

import requests
from typing import Iterable

from concurrent.futures import ThreadPoolExecutor, as_completed, Future


def safe_get(*args, **kwargs):
  """Wraps `request.get` but always returns exceptions as strings."""
  try:
    r = requests.get(*args, **kwargs)
    return r
  except Exception as exc:
    return str(exc)


URLS = [
  'http://www.foxnews.com/', # 200
  'http://www.cnn.com/', # 200
  'http://europe.wsj.com/', # 403
  'http://www.bbc.co.uk/', # 200
  'http://nonexistant-subdomain.python.org/' # max retry error
]


n_threads = 4


def example_as_completed():
  with ThreadPoolExecutor(max_workers=n_threads) as pool:
    # Tasks are submitted to the pool to be processed.
    # Each submission returns a `Future` object.
    # We store a dict here to remember which future corresponds to each URL.
    future_to_url = {pool.submit(requests.get, url, timeout=5): url for url in URLS}

    # Iterator over futures - they are returned as completed, not necessarily in
    # the order they were started. This can take in any iterable (list, dict, etc).
    for future in as_completed(future_to_url):
      url = future_to_url[future]
      try:
        r = future.result()
        print(url, r.status_code)
      except Exception as exc:
        print(url, exc)


def all(futures: Iterable[Future]) -> list:
  """Gathers all results from a list of futures and returns them."""
  return [f.result() for f in futures]


def example_wait_all():
  with ThreadPoolExecutor(max_workers=n_threads) as pool:
    future_to_url = {pool.submit(safe_get, url, timeout=5): url for url in URLS}
    # results = [(url, f.result()) for f, url in future_to_url.items()]
    # print(results)
    results = all(future_to_url)
    print(results)
    # for future in future_to_url:
      # future.result()
    

t0 = time.time()
example_wait_all()
print(f"elapsed: {time.time() - t0:.3f}s")


t0 = time.time()
example_as_completed()
print(f"elapsed: {time.time() - t0:.3f}s")