#!/usr/bin/env python3
"""Module for the async_comprehension coroutine."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehension.

    Uses an async comprehension over async_generator to gather
    10 random floats and returns them as a list.
    """
    return [i async for i in async_generator()]
