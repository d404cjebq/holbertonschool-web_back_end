#!/usr/bin/env python3
"""Module for the measure_time function."""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average runtime of wait_n(n, max_delay).

    Runs wait_n synchronously via asyncio.run, times the total
    execution using the time module, and returns total_time / n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
