#!/usr/bin/env python3
""" This is a module Annotate the below function’s parameters and return
values with the appropriate types """


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ This return the calculated value """
    return [(i, len(i)) for i in lst]
