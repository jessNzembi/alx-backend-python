#!/usr/bin/env python3
""" type-annotated function """

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ the function """
    if lst:
        return lst[0]
    else:
        return None
