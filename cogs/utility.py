import discord
from discord.ext import commands

class Utility(commands.Cog, description='Only my *true* kouhai can use me, but I don\'t mind if others find utility in me. 👉 👈'):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases=['colour'], description='Sets your role color.', help='This uses discord\'s implementation of colors. As such, hex codes must be prefixed with `#`. Additionally, you can use pre-specified colors such as `red` or `blue` etc.')
    async def color(self, ctx, color: discord.Colour):
        role = discord.utils.get(ctx.guild.roles, name=f'{ctx.author.id}')
        if role is None:
            role = await ctx.guild.create_role(name=f'{ctx.author.id}', color=color)
            await ctx.author.add_roles(role)
            return await ctx.send(f'Your role has been created and updated to {color}.')
        await role.edit(colour=color)
        if role not in ctx.author.roles:
            await ctx.author.add_roles(role)
        await ctx.send(f'Your role has been updated to {color}.')

    @color.error
    async def color_error(self, ctx, error):
        if isinstance(error, commands.BadColourArgument):
            await ctx.reply('That doesn\'t seem to be a valid color.')

async def setup(bot):
    await bot.add_cog(Utility(bot))
