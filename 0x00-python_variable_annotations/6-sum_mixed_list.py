#!/usr/bin/env python3
"""
This is a module that pass a list of data type int, float then return a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ This return the sum of the mix list """
    return sum(mxd_lst)
