"""
Example Bot written by Stig [2648238]

This file has an example of a @task.loop

These are extremely useful, and are triggered after time has past, you can also schedule these which I have provided an example of below

Use API Reference for more info:
https://docs.pycord.dev/en/stable/ext/tasks/index.html
"""

import asyncio
from datetime import datetime

from discord.ext import commands, tasks


class Loops(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.clock.is_running():
            self.clock.start()

    @tasks.loop(minutes=5)
    async def clock(self):
        self.bot.logger.debug("+1 Nerve")

    @clock.before_loop
    async def before_clock(self):
        for _ in range(86400):
            # If current minute has no remainder after being divided by 5, ie 5, 10, 15, 20, and the current second is 0, start loop
            if not datetime.utcnow().minute % 5 and datetime.utcnow().second == 0:
                return
            await asyncio.sleep(1)  # Wait 1 second and try again


def setup(bot):
    bot.add_cog(Loops(bot))
