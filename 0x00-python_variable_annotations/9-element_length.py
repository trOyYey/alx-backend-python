#!/usr/bin/env python3
'''
9-element_length.py module
'''
from typing import List, Tuple, Iterable, Sequence

return_type = List[Tuple[Sequence, int]]


def element_length(lst: Iterable[Sequence]) -> return_type:
    ''' return values with the appropriate types of the given function '''
    return [(i, len(i)) for i in lst]
