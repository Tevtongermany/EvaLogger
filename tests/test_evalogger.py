import requests
import aiohttp
import asyncio
import pytest
import sys

sys.path.append("/evalogger")

import evalogger


def test_functionality():
    log = evalogger.EvaLogger()
    log.info("Hello World!")
    log.warn("Hello World!")
    log.error("Hello World!")
    log.exception_error(RuntimeError("Hello World!"))
    log.success("Hello World!")
    log.network(requests.get("https://google.com"))
    log.network(requests.get("https://google.com"), text="Google")
    log.info("Spacing \n\n")


@pytest.mark.asyncio
async def test_async_functionality():
    log = evalogger.EvaLogger()
    log.info("Hello Async World! ")
    log.warn("Hello Async World!")
    log.error("Hello Async World!")
    log.exception_error(RuntimeError("Hello Async World!"))
    log.success("Hello Async World!")
    async with aiohttp.ClientSession() as session:
        async with session.get("https://google.com") as response:
            log.network(response)
            log.network(response, text="Google")


test_functionality()
asyncio.run(test_async_functionality())
