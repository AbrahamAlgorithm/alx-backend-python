#!/usr/bin/env python3
'''A coroutine will collect 10 random numbers'''


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Returns the 10 random numbers'''
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.perf_counter() - start_time
    return (end_time)
