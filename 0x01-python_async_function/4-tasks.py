
#!/usr/bin/env python3
'''
4-tasks.py module
'''
import asyncio
from typing import List

taskR = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of floats of running wait_random n number of times

    Parameters
    ----------
    n: int
        number of times to run wait_random
    max_delay: int
        maximum delay each coroutine could have

    Returns
    -------
    List[float]
        a list of floats of the executed functions
    """
    output: List[float] = [taskR(max_delay) for a in range(n)]
    return [
        await func
        for func in asyncio.as_completed(output)
    ]
