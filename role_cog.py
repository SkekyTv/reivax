import discord

from discord.ext import commands
import re

from pprint import pprint

class role_cog(commands.Cog):
    def __init__(self, bot, default_guild):
        self.bot = bot
        self.default_guild = default_guild

    @commands.command(name="add_role", help="Add selected role to selected usr")
    async def add_role(self, ctx, *args):
        guild = self.bot.get_guild(int(self.default_guild))
        role = guild.get_role(int(re.sub("[^0-9]","",args[1])))
        pprint(role)
        pprint(int(re.sub("[^0-9]","",args[0])))
        member = guild.get_member(int(re.sub("[^0-9]","",args[0])))
        await member.add_roles(role)

    @commands.command(name="remove_role", help="Remove selected role to selected usr")
    async def remove_role(self, ctx, *args):
        guild = self.bot.get_guild(int(self.default_guild))
        role = guild.get_role(int(re.sub("[^0-9]","",args[1])))
        pprint(role)
        pprint(int(re.sub("[^0-9]","",args[0])))
        member = guild.get_member(int(re.sub("[^0-9]","",args[0])))
        await member.remove_roles(role)

