#!/usr/bin/env python3
'''
101-safely_get_value.py module
'''
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    ''' returns the value in key index or None in safely manner'''
    if key in dct:
        return dct[key]
    else:
        return default
