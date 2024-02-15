#!/usr/bin/env python3
""" type-annotated function """

from typing import List


def sum_list(mxd_list: List[int, float]) -> float:
    """ the function """
    return sum(mxd_list)
