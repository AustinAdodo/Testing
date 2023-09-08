import unittest

# from Testing.main import count_primes_less_than, sieveofEratosthenes


class Cases(unittest.TestCase):
    def test_my_method1(self):
        self.assertEqual(34, 11)


if __name__ == '__main__':
    unittest.main()

# Utilizing multiple CPU cores in a Python program can improve the performance and reduce the execution time of
# CPU-bound tasks, such as data processing, machine learning, and scientific computing. Here are some ways to achieve
# this:
#
# Multiprocessing: The multiprocessing module in Python allows you to spawn multiple processes and utilize all
# available CPU cores to execute the task in parallel. Each process runs independently of others and can access its
# own memory space. This is useful when you have a CPU-bound task that can be split into multiple independent subtasks.
#
# Threading: The threading module in Python allows you to spawn multiple threads within a process and execute them
# concurrently. Each thread shares the same memory space as the main thread, so they can access and modify the same
# variables. This is useful when you have an I/O-bound task, such as web scraping or downloading files,
# where the threads can be used to perform non-blocking I/O operations.
#
# Concurrent.futures: The concurrent.futures module in Python provides a high-level interface for asynchronously
# executing functions using threads or processes. It provides a ThreadPoolExecutor and ProcessPoolExecutor classes,
# which allows you to execute functions in parallel and asynchronously wait for the results.
#
# Dask: Dask is a parallel computing library in Python that can scale computation on clusters of computers. It
# provides a high-level interface to parallelize Python code using task scheduling and data parallelism. This is
# useful when you have a task that cannot fit in the memory of a single machine and needs to be executed on a cluster
# of machines.
#
# The need to utilize multiple CPU cores in a Python program depends on the type of task and the size of the data. If
# the task involves heavy computation or large amounts of data, it can benefit from parallel processing. On the other
# hand, if the task is I/O-bound, such as network or disk I/O, parallel processing may not be necessary.
