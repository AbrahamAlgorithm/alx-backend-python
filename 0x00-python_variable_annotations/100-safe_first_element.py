#!/usr/bin/env python3
'''The types of the elements of the input are not know'''


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''The types of the elements of the input are not know'''
    if lst:
        return lst[0]
    else:
        return None
