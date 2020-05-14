import discord
from discord.ext import commands
from cogs.utils import imgmanip


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def waaw(self, ctx):
        """Mirrors an image from the left side"""
        workImg = await imgmanip.openImg(ctx.message.attachments[0].url)
        imgOut = imgmanip.lMirror(workImg)
        await ctx.send(file=discord.File(imgOut))

    @commands.command()
    async def haah(self, ctx):
        """Mirrors an image from the right side"""
        workImg = await imgmanip.openImg(ctx.message.attachments[0].url)
        imgOut = imgmanip.rMirror(workImg)
        await ctx.send(file=discord.File(imgOut))

    @commands.command()
    async def woow(self, ctx):
        """Mirrors an image from the top side"""
        workImg = await imgmanip.openImg(ctx.message.attachments[0].url)
        imgOut = imgmanip.tMirror(workImg)
        await ctx.send(file=discord.File(imgOut))

    @commands.command()
    async def hooh(self, ctx):
        """Mirrors an image from the bottom side"""
        workImg = await imgmanip.openImg(ctx.message.attachments[0].url)
        imgOut = imgmanip.bMirror(workImg)
        await ctx.send(file=discord.File(imgOut))


def setup(bot):
    bot.add_cog(Images(bot))
