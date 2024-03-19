#!/usr/bin/env python3
""" This is a module that Write a coroutine called async_generator that takes
no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then
yield a random number between 0 and 10. Use the random module.
"""


import asyncio
import random


async def async_generator():
    """ This is a function that geneate a random number """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def print_yielded_values():
    """ This is a function that return the value """
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
