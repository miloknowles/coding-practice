# Python Concurrency

When should you use multithreading vs. multiprocessing?
- Multithreading is useful when the program is IO-bound and spends a lot of time waiting for slow external services (e.g APIs, read/write, user input). Note that it WILL NOT make heavy CPU workloads any faster, since the total amount of CPU cores available to a multithreaded applications remains the same.
- Multiprocessing, on the other hand, is useful when the program is CPU-bound, and needs to do a lot of CPU-intensive work. Each additional process has access to another CPU core.

## Multithreading

Multithreading can be implemented in several ways in Python:
- Using the `async` and `await` syntax, and then dispatching workers with the `asyncio` package. This has fairly convenient syntax, and seems nicer than working with `threading`.
- Using the `threading` package, which allows you to start threads and wait for their results. I've found it useful to use threads with Python's `queue` package. You can have several threads run and pull jobs off of a shared queue. I'm not sure yet how you easily gather all the results from the threads. Maybe putting the results on an output queue?
- Using the `ThreadPoolExecutor`, which also has very convenient syntax. So far this is my favorite due to ease of use. There are some nice features, like `map`-ing tasks, and iterating over tasks as they complete with `as_completed`. It's easy to get the results for each task with `result()`.

## Multiprocessing
