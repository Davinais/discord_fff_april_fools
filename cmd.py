from discord.ext import commands
from discord.utils import get

class Cmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.bot.command()(self.shutdown)
        self.bot.command()(self.join)
        self.bot.command()(self.leave)

    async def shutdown(self, ctx):
        if (await ctx.bot.is_owner(ctx.author)):
            await ctx.bot.logout()

    async def join(self, ctx):
        channel = ctx.author.voice.channel
        vc = ctx.voice_client
        if vc and vc.is_connected():
            await ctx.voice_client.move_to(channel)
        else:
            await channel.connect()

    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

def setup(bot):
    bot.add_cog(Cmd(bot))