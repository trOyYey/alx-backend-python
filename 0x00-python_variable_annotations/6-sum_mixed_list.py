#!/usr/bin/env python3
'''
6-sum_mixed_list.py module
'''
from functools import reduce
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    ''' returns sum of all mixed values within the list '''
    return reduce(lambda a, b: a + b, input_list)
