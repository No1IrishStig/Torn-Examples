"""
Example Bot written by Stig [2648238]

This file has two examples of Slash Commands
- Custom Help Command
- Basic Verify Command
- Embed Message Command

Slash commands are 'interactions' and you must respond to them within 3 seconds otherwise you will see an 'Interaction Failed' message in discord

If your code takes longer than 3 seconds to execute, you can use .defer() extend that 3 second wait, and then follow up with a response later

For custom embed colors, hex is used, example #000000 however the # is changed to 0x, so it ends up as 0x000000

Use API Reference for more info:
https://docs.pycord.dev/en/stable/api/models.html
"""

import discord
import json

from discord.ext import commands
from Utilities import Functions


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Storing a Dictionary of Commands for the Custom Help Command
        self.commands = {
            "Public": {
                "help": "This command",
                "verify": "Verify your Torn account with your Discord account",
                "invite": "Invite this bot to a server",
            },
            "Private": {
                "clear [count]": "Clear messages from a channel",
            },
        }

        self.verified_users = {}

    @commands.slash_command(description="Help Slash Command")  # Stating this will be a Slash Command with its description
    @commands.cooldown(1, 10, commands.BucketType.user)  # Adding a cooldown so it cannot be spammed
    async def help(self, ctx):  # Defining the name of the Slash Command (help) with required arguments (self, ctx)
        embed = discord.Embed(colour=0xe4ebe8, title=f"{self.bot.user.name} Bot Help")
        embed.add_field(name="Public", value="\n".join(f"`{k}` - {v}" for k, v in self.commands['Public'].items()), inline=False)
        embed.add_field(name="Private", value="\n".join(f"`{k}` - {v}" for k, v in self.commands['Private'].items()), inline=False)
        await ctx.send(embed=embed)

    @commands.slash_command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def verify(self, ctx):
        if ctx.author.id in self.verified_users:
            tornUser = self.verified_users[ctx.author.id]
            return await ctx.respond(f"You are already verified as {tornUser['name']} [{tornUser['player_id']}]")  # Adding an f at the start of Strings allows for inline variable usage

        data = await Functions.request(f"https://api.torn.com/user/{ctx.author.id}?selections=discord,profile&key={self.bot.key}")  # Making API Call using stored API Key from the config

        if not data:
            return await ctx.respond("No response from the API", "Error")

        if "error" in data:  # If Torn returned an error code
            if data["error"]["code"] == 6:
                return await ctx.respond(f"You are not Torn Verified, do this in their discord")
            else:
                return await ctx.respond(f"Torn responded unexpectedly:\n\n```json\n{json.dumps(data, indent=4, sort_keys=True)}```")

        # Adding Player to verified_users dictionary
        # Dictionaries are NOT PERSISTENT meaning their contents will be erased when the bot is restarted
        # Consider using a .json file, or a database to store data permanently
        self.verified_users[ctx.author.id] = data
        await ctx.respond(f"Hello, {data['name']} [{data['player_id']}] your discord account has been Verified!")

    @commands.slash_command(description="Delete messages out of a Channel")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: discord.Option(int, description="The number of messages to delete", min_value=1, max_value=100)):
        deleted_count = await ctx.channel.purge(limit=amount)
        await ctx.respond(f"Deleted: {len(deleted_count)} messages", delete_after=15)  # Self Deletes after 15 seconds


    """
    This command will find an item using the API and give you data about it
    
    Heres a sample of the API response:
    
    {
        "items": {
            "1": {
                "name": "Hammer",
                "description": "A small, lightweight tool used in the building industry. Can also be used as a weapon.",
                "effect": "",
                "requirement": "",
                "type": "Melee",
                "weapon_type": "Clubbing",
                "buy_price": 75,
                "sell_price": 50,
                "market_value": 22,
                "circulation": 2149861,
                "image": "https://www.torn.com/images/items/1/large.png",
            }
        }
    }
    """

    @commands.slash_command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def item(self, ctx, name: discord.Option(str, required=True, description="The Item to Look For")):
        tornItems = await Functions.request(f"https://api.torn.com/torn/?selections=items&key={self.bot.key}")  # Making API Call using stored API Key from the config

        if not tornItems:
            return await ctx.respond("No response from the API", "Error")

        if "error" in tornItems:  # If Torn returned an error code
            return await ctx.respond(f"Torn responded unexpectedly:\n\n```json\n{json.dumps(tornItems, indent=4, sort_keys=True)}```")

        for itemID, itemData in tornItems['items'].items():  # Looping through Key: Value pairs
            if itemData['name'].lower() == name.lower():
                embed = discord.Embed(colour=0xe4ebe8, description=itemData['description'])
                embed.set_author(name=f"{itemData['name']} [{itemID}]")

                if itemData.get('weapon_type', None):  # If it's a weapon with a valid weapon_type
                    embed.add_field(name="Type", value=f"{itemData['type']} - {itemData['weapon_type']}")
                else:
                    embed.add_field(name="Type", value=itemData['type'])

                embed.add_field(name="Circulation", value=format(itemData['circulation'], ','))  # Formatting adds commas for billions, millions, thousands etc
                embed.add_field(name="Market Value", value=f"${format(itemData['market_value'], ',')}")
                embed.set_thumbnail(url=itemData['image'])

                if itemData['effect'] != "":  # If effect is not equal to "" add it to the footer
                    embed.set_footer(text=f"Effect: {itemData['effect']}")

                return await ctx.respond(embed=embed)

        # Code will only get here if no item is found with the name
        return await ctx.respond(embed=discord.Embed(colour=0xE43434, description=f"Item with name {name} not found!"))


def setup(bot):
    bot.add_cog(Commands(bot))
