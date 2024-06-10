#!/usr/bin/env python
import asyncio
import List from typing
import wait_random from 0-basic_async_syntax.py
'''An async routine called wait_n that takes in 2 int arguments'''


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))

    sorted_delays = []
    while delays:
        min_delay = min(delay)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays

