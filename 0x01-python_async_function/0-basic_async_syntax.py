#!/usr/bin/env python3
""" module containing asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10):
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
