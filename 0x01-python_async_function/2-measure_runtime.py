#!/usr/bin/env python3
'''
2-measure_runtime.py module
'''
import asyncio
import time

waitN = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns the calculated average time it takes to run the function
    wait_n n times.

    Arguments:
        n: The number of times to execute the coroutine
        max_delay: The maximum delay each coroutine call should have

    Returns:
        The average time it takes to run the coroutine
    """
    start: float = time.perf_counter()
    asyncio.run(waitN(n, max_delay))
    end: float = time.perf_counter() - start
    return end / n
