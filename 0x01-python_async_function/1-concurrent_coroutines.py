""" This is a module that takes in 2 int arguments (in this order): n and
max_delay. You will spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values). The list of
the delays should be in ascending order without using sort() because of
concurrency.
"""


import asyncio
from typing import List
from random import uniform
from asyncio import Task


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ This function return the list of all delays in float value """

    delays = []
    tasks: List[Task[float]] = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
