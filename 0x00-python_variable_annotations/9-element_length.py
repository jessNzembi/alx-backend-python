#!/usr/bin/env python3
""" type-annotated function """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ the function """
    return [(i, len(i)) for i in lst]
