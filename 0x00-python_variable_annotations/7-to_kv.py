#!/usr/bin/env python3
'''
7-to_kv.py module
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' returns  (k, v*v) as a tuple'''
    return (k, v * v)
