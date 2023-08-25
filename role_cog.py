import discord

from discord.ext import commands

from id_formatter import id_str_to_int


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
        role = guild.get_role(role_id)
        member = guild.get_member(user_id)
        return [member, role]

    @commands.command(name="add_role", help="Add selected role to selected usr")
    async def add_role(self, ctx, *args):
        member, role = self.get_ressources(
            user_id=id_str_to_int(args[0]), role_id=id_str_to_int(args[1])
        )
        await member.add_roles(role)

    @commands.command(name="remove_role", help="Remove selected role to selected usr")
    async def remove_role(self, ctx, *args):
        member, role = self.get_ressources(
            user_id=id_str_to_int(args[0]), role_id=id_str_to_int(args[1])
        )
        await member.remove_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        role = self.bot.get_guild(int(self.default_guild)).get_role(1143818338707984424)
        await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        member, role = self.get_ressources(
            user_id=payload.user_id, role_id=1143818338707984424
        )
        await member.remove_roles(role)
