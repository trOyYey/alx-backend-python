#!/usr/bin/env python3
'''
3-tasks.py module
'''
import asyncio

waitR = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a task that runs the `wait_random` coroutine once

    Parameters
    ----------
    max_delay : int
        The maximum delay the coroutine could have

    Returns
    -------
    asyncio.Task
        The execution of  `wait_random`

    """
    return asyncio.create_task(waitR(max_delay))
