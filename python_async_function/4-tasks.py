#!/usr/bin/env python3

""" task_wait_n function"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times with the specified max_delay 
    and returns the list of all the delays in ascending order.

    Args:
        n: Number of times to run
        max_delay: Max delay time

    Returns:
        List of values in ascending order
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays