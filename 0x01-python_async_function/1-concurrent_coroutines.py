#!/usr/bin/env python3
'''
1-concurrent_coroutines.py module
'''

import asyncio
from typing import List

waitRandom = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of floats of running waitRandom n number of times

    Parameters
    ----------
    n: int
        number of times to run the coroutine
    max_delay: int
        maximum delay for waitrandom function

    Returns
    -------
    List[float]
        a contains the floats of random waitings
    """
    delaylist: List[float] = [waitRandom(max_delay) for a in range(n)]
    return [
        await func
        for func in asyncio.as_completed(delaylist)
    ]
