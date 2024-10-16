#!/usr/bin/env python3
'''
1-async_comprehension.py module
'''

from typing import List

asyncG = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    calls  async_generator coroutine

    Returns:
        A list of 10 random float values between 0 and 10
    """
    return [i async for i in asyncG()]
