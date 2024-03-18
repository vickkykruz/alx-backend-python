#!/usr/bin/env python3
"""
This is a moduke that create a measure_time function with integers n and
max_delay as arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n. Your function should return
a float.

Use the time module to measure an approximate elapsed time.
"""


from time import time
from asyncio import run


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """ This is return the total execution time """

    start_time = time()
    run(wait_n(n, max_delay))
    end_time = timer()
    total_time = end_time - start_time
    return total_time / n
