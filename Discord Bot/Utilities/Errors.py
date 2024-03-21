"""
Example Bot written by Stig [2648238]

This file has an example of an error handler for Slash Commands

These are required to give people feedback on what happened with their command when an error occurs

Use API Reference for more info:
https://docs.pycord.dev/en/stable/ext/commands/commands.html#error-handling
"""

import traceback
import discord

from discord.ext import commands


class Errorhandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ignored = (commands.CommandNotFound, commands.NoPrivateMessage, commands.DisabledCommand, discord.NotFound, commands.BadArgument)

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        attrerror = getattr(error, "original", error)

        if isinstance(attrerror, self.ignored):
            return

        if isinstance(attrerror, commands.CommandOnCooldown):
            return await ctx.respond(f"{ctx.author.mention}, you need to wait {round(error.retry_after, 2)} seconds before you can use this command again!", ephemeral=True)  # Ephemeral means only the command sender can see this message

        elif isinstance(attrerror, commands.MissingPermissions):
            try:
                return await ctx.respond("You are not permitted to do that")
            except discord.Forbidden:
                pass

        if isinstance(attrerror, discord.Forbidden):
            try:
                return await ctx.respond("Im not permitted to do that")
            except discord.Forbidden:
                pass

        # Unhandled

        result = "".join(traceback.format_exception(error, error, error.__traceback__))
        await ctx.send(f"Something went wrong. Try again later:\n\n```py\n{result[:1800]}```")  # Sends Traceback limited to 1800 characters (Max 2000 per message)


def setup(bot):
    bot.add_cog(Errorhandler(bot))
