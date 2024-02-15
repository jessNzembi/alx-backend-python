#!/usr/bin/env python3
""" type-annotated function """

from typing import Mapping, Any, TypeVar, Optional

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Optional[T] = None
) -> Optional[T]:
    """ the function """
    return dct.get(key, default)
