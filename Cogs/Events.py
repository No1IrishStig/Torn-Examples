"""
Example Bot written by Stig [2648238]

This file has an example of an Event Handlers
- on_message
- on_member_join

These contain a welcomer and a greetings replier

Events are triggered when something happens, such as a member joining a server, changing their name, sending a message etc

Use API Reference for more info:
https://docs.pycord.dev/en/stable/api/events.html
"""

from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):  # Notice, no ctx here
        if not message.guild or message.author.bot:  # Ignoring Bots and DMs
            return

        greetings = ['hello', 'hi', 'hey', 'howdy', 'hiya']
        for greeting in greetings:  # Looping over each greeting in the list above
            if greeting in message.content.lower():  # If one is in the message content (converted to all lower case), reply to the message
                return await message.reply(f"{greeting.title()}, {message.author.name}!")  # Respond with the same greeting with the first letter capitalised
                # Returning so it doesn't send multiple replies if the message contains multiple

    @commands.Cog.listener()
    async def on_member_join(self, member):  # Notice, no ctx here
        if not member.guild or member.bot:  # Ignoring Bots and DMs
            return

        welcome_channel = member.guild.text_channels[0]  # Selecting the First Text Channel out of a list

        # To set a different, specific channel, you can copy the ID of the channel and then use the following:
        # welcome_channel = self.bot.fetch_channel(Channel_ID)
        return await welcome_channel.send(f"Welcome to {member.guild.name}, {member.mention}!")  # Respond with the same greeting with the first letter capitalised


def setup(bot):
    bot.add_cog(Events(bot))
