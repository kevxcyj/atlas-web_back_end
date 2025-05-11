#!/usr/bin/env python3

""" async_comprehenion function """

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collects 10 random numbers using an async comprehension over async_generator.

    Returns:
        List containing 10 numbers
    """

    result = [i async for i in async_generator()]

    return result
