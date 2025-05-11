#!/usr/bin/env python3

"""measure_time function"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Measures the total execution time for wait_n(n, max_delay).

    Args:
        n: NUmber of calls for wait-n
        max_delay: Max delay time

    Returns:
        Time taken to call n
    """

    start_time = time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time()

    return (end_time - start_time) / n
