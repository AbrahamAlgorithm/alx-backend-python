#!/usr/bin/env python
'''An async routine called wait_n that takes in 2 int arguments'''


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''An async function'''
    delays = []
    for _ in range(n):
        value = asyncio.create_task(wait_random(max_delay))
        delays.append(value)
    val = [await r for r in asyncio.as_completed(delays)]
    return val
