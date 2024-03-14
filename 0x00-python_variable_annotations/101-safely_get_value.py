#!/usr/bin/env python3
"""
This is a module that return values, add type annotations.
"""


from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)-> Union[Any, T]:
    """ This return values, add type annotations to the function """
    if key in dct:
        return dct[key]
    else:
        return default
