#!/usr/bin/env python3

""" async_generator function """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times, wait 1 second,
        then yield a random number between 0 and 10.

    Returns:
        Float between 1 and 0
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
