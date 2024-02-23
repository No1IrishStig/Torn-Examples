"""
Example Bot written by Stig [2648238]

This file contains some basic functions

Use API Reference for more info:
https://docs.pycord.dev/en/stable/api/index.html
"""

import aiohttp
import json


def getConfig():  # Getting the config file
    with open('Utilities/config.json', encoding="utf8") as data:
        return json.load(data)


config = getConfig()


async def request(url):  # Async API Requesting so it doesn't lock up the bot if its taking longer than expected
    url = url + f"&comment={config['api_request_comment']}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()
