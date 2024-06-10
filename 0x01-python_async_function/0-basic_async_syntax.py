#!/usr/bin/env python3
import asyncio
import random
'''asynchronous coroutine that takes in an integer argument'''


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
