#!/usr/bin/env python3
'''A coroutine called async_generator that takes no arguments.'''


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    '''The coroutine will loop 10 times'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
