#!/usr/bin/env python3
""" This is a module that write a coroutine called async_comprehension that
takes no arguments.
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ This is a function that return value in an aynsc comprehension """
    return [num async for num in async_generator()]
