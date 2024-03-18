#!/usr/bin/env python3
"""
This is a module that nearly identical to wait_n except task_wait_random is
being
"""


import asyncio
from asyncio import Task
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ This return nearly identical to wait_n except task_wait_random is
        being
    """

    delays = []
    tasks: List[Task[float]] = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
