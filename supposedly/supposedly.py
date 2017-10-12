import discord
import asyncio
from discord.ext import commands
from random import randint

__author__ = "SinisterPyro"

class Supposedly:
    """Supposedly Addon"""

    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        server = message.server
        channel = message.channel
        author = message.author
        randomInt = randint(0, 300)
        if message.server is None:
            return
        if author == self.bot.user:
            return
        if randomInt == 0:
            await self.bot.send_message(channel, "*Supposedly...*")

def setup(bot):
    bot.add_cog(Supposedly(bot))
