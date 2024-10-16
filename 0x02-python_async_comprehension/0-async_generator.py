#!/usr/bin/env python3
'''
0-async_generator.py
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine generates randomv values between 0 and 10.

    sleeps for a random value between 0 and 10 seconds
    then returns it.

    looping 10 times.

    Returns:
        A list of 10 random float values from 1 to 10
    """
    for i in range(10):
        # sleep for 1 seond
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
