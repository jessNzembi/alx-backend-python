#!/usr/bin/env python3
""" type-annotated function """


from typing import Tuple, List


def zoom_array(numbers: Tuple[int], factor: int = 2) -> List[int]:
    """ the function """
    return [num for num in numbers for _ in range(factor)]


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)

print(zoom_2x)
print(zoom_3x)
