#!/usr/bin/env python3
""" type-annotated function """

from typing import List, Union


def sum_list(mxd_list: List[Union[int, float]]) -> float:
    """ the function """
    return sum(mxd_list)
