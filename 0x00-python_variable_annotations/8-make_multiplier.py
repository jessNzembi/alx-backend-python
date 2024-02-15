#!/usr/bin/env python3
""" type-annotated function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ the function """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
