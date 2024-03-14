#!/usr/bin/env python3
""" This is a module that orrect duck-typed annotations: """


from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ This return the first index in the list or None"""
    if lst:
        return lst[0]
    else:
        return None
