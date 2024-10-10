#!/usr/bin/env python3
'''
100-safe_first_element.py module
'''
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    ''' return first element of a list or none if list is empty  '''
    if lst:
        return lst[0]
    else:
        return None
