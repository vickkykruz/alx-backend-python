#!/usr/bin/env python3
""" This is a module that  takes a float multiplier as argument and returns a
function that multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This return a function multipler_func """
    def multiplier_func(x: float) -> float:
        """ This return the multplier of x """
        return x * multiplier
    return multiplier_func
