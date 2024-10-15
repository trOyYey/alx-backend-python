#!/usr/bin/env python3
'''
0-basic_async_syntax.py module
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
        coroutine that sleeps in random time between
        0 and 10 or argument value then returns it
    '''
    RandomDelay: float = random.uniform(0, max_delay)
    await asyncio.sleep(RandomDelay)
    return RandomDelay
