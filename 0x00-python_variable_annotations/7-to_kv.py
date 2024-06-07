#!/usr/bin/env python3
'''Python Variable annotation is the very best way to go'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Python annotation is the very best way to go'''
    value = tuple([k, v * v])
    return value
