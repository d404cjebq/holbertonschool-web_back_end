#!/usr/bin/env python3
"""Module for the task_wait_random function."""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio.Task for wait_random(max_delay).

    Wraps the wait_random coroutine in a Task so it can be
    scheduled to run on the event loop.
    """
    return asyncio.create_task(wait_random(max_delay))
