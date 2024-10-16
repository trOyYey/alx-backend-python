#!/usr/bin/env python3
'''
2-measure_runtime.py module
'''

import asyncio
from time import perf_counter

asyncC = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of the async_comprehension coroutine.

    Returns:
        time spent to run the async_comprehension coroutine.
    """
    # start measuring the time
    start = perf_counter()
    await asyncio.gather(*[asyncC() for i in range(4)])

    # deduct current time from starting time to measure time spent executing
    return perf_counter() - start
