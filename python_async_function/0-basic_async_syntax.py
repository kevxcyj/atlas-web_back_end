#!/usr/bin/env python3

""" wait_random function """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that takes in an
        integer argument, waits for delay, then returns.

    Args:
        max_delay (int): Max delay time

    Returns:
        float: Seconds waited
    """

    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
