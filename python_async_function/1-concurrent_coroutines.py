#!/usr/bin/env python3
"""Module for the wait_n coroutine."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.

    Runs n instances of wait_random concurrently and returns
    the list of delays in ascending order, without using sort(),
    by awaiting each coroutine as it completes.
    """
    delays = []
    coroutines = [wait_random(max_delay) for _ in range(n)]
    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)
    return delays
