#!/usr/bin/env python3
'''Python is very good in Variable annotation'''

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Python is very good in variable annotation '''
    return [(i, len(i)) for i in lst]
