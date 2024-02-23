"""
Example Bot written by Stig [2648238]

This is the main bot file which you must run to bring the bot online

In the Cogs folder there are a few example files containing:
- 4 Slash Commands
- 2 Event Listeners
- 1 Tasked Loop

This should provide a solid basis to begin your own bot development journeys. If you need additional help, feel free to contact me on Torn!

Use API Reference for more info:
https://docs.pycord.dev/en/stable/api/index.html
"""

import discord
import os

from discord.ext import bridge
from Utilities import Functions, Logger


bot = bridge.Bot(command_prefix='!', intents=discord.Intents.all())  # Creating the Bot Instance
bot.logger = Logger.startLogging()  # Starting Logging and storing it inside the Bot Object
bot.config = Functions.getConfig()  # Storing the config in the Bot object
bot.key = bot.config['api_key']  # Setting Global Variable 'Key' inside the Bot object, can be accessed in most places where the 'bot' instance is assessable

bot.logger.debug(" ---------------------------------- ")
bot.logger.debug("| Debug!                           |")
bot.logger.info("| Info!                            |")
bot.logger.warning("| Warning!                         |")
bot.logger.error("| Error!                           |")
bot.logger.critical("| Critical!                        |")
bot.logger.debug(" ---------------------------------- ")


@bot.check
async def globalChecks(ctx):  # Conditions that are checked on every command run
    if not ctx.guild:
        return await ctx.respond("Commands are disabled in my private messages, sorry!")

    return True


@bot.event
async def on_ready():  # Runs whenever the bot is Ready
    bot.logger.warning(f'Use CTRL + C in the Terminal to end the bot')
    bot.logger.info(f'Logged in as: {bot.user.name}\n{len(bot.extensions)} Cogs Loaded')  # Logs to Console
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Torn Players"))  # Updates Bot Activity

bot.load_extension("Utilities.Errors")  # Load Error Handler
for file in os.listdir(f"Cogs"):  # Loops through all .py files in the 'Cogs' folder and loads them
    if file.endswith(".py"):
        bot.load_extension(f"Cogs.{file[:-3]}")

bot.run(bot.config['token'], reconnect=True)  # Runs the Bot using the token from the Config file
