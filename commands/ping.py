from discord.ext import commands


class HelloCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def hello(self, ctx):
        await ctx.send(f"Hello, {ctx.author.mention}!")


def setup(bot):
    bot.add_cog(HelloCommand(bot))
