#!/usr/bin/env python3
"""Module for the wait_random coroutine."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds.

    Sleeps asynchronously for a randomly generated float number
    of seconds, uniformly distributed between 0 and max_delay,
    and returns that delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
