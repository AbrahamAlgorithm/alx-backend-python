#!/usr/bin/env python3
'''The coroutine will collect 10 random numbers using an async comprehensing'''


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''return the 10 random numbers'''
    return [value async for value in async_generator()]
