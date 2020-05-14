import discord
from discord.ext import commands
from cogs.utils import imgmanip


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def waaw(self, ctx):
        """Mirrors an image from the left side"""
        try:
            workImg = await imgmanip.openImg(ctx.message.attachments[0].url)
            imgOut = imgmanip.ultiMirror(workImg, 'l')
            await ctx.send(file=discord.File(imgOut))
        except IndexError:
            await ctx.send('No image found! :(')

    @commands.command()
    async def haah(self, ctx):
        """Mirrors an image from the right side"""
        try:
            workImg = await imgmanip.openImg(ctx.message.attachments[0].url)
            imgOut = imgmanip.ultiMirror(workImg, 'r')
            await ctx.send(file=discord.File(imgOut))
        except IndexError:
            await ctx.send('No image found! :(')

    @commands.command()
    async def woow(self, ctx):
        """Mirrors an image from the top side"""
        try:
            workImg = await imgmanip.openImg(ctx.message.attachments[0].url)
            imgOut = imgmanip.ultiMirror(workImg, 't')
            await ctx.send(file=discord.File(imgOut))
        except IndexError:
            await ctx.send('No image found! :(')

    @commands.command()
    async def hooh(self, ctx):
        """Mirrors an image from the bottom side"""
        try:
            workImg = await imgmanip.openImg(ctx.message.attachments[0].url)
            imgOut = imgmanip.ultiMirror(workImg, 'b')
            await ctx.send(file=discord.File(imgOut))
        except IndexError:
            await ctx.send('No image found! :(')


def setup(bot):
    bot.add_cog(Images(bot))
