import discord

from discord.ext import commands
import re


class role_cog(commands.Cog):
    def __init__(self, bot, default_guild):
        self.bot = bot
        self.default_guild = default_guild

    def get_ressources(self, user_id, role_id):
        """Get the user and roel entity from the bot guild

        Args:
            user_id (int): the wanted user's id
            role_id (int): the wanted role's id

        Returns:
            ressources ([User, Role]): the wanted user and role entity
        """
        guild = self.bot.get_guild(int(self.default_guild))
        role = guild.get_role(int(re.sub("[^0-9]", "", role_id)))
        member = guild.get_member(int(re.sub("[^0-9]", "", user_id)))
        ressources = [member, role]
        return ressources

    @commands.command(name="add_role", help="Add selected role to selected usr")
    async def add_role(self, ctx, *args):
        member, role = self.get_ressources(user_id=args[0], role_id=args[1])
        await member.add_roles(role)

    @commands.command(name="remove_role", help="Remove selected role to selected usr")
    async def remove_role(self, ctx, *args):
        member, role = self.get_ressources(user_id=args[0], role_id=args[1])
        await member.remove_roles(role)

