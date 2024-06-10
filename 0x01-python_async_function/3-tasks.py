#!/usr/bin/env python3
'''A func that takes an int and returns a asyncio.Task'''


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> int:
    '''An async function'''
    return asyncio.create_task(wait_random(max_delay))
