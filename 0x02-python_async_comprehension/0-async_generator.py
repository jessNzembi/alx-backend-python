#!/usr/bin/env python3
"""async comprehension"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """An asynchronous generator yielding random floats."""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
