#!/usr/bin/env python3
"""Module for the async_generator coroutine."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously generate 10 random numbers.

    Loops 10 times, asynchronously waiting 1 second each time,
    then yields a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
