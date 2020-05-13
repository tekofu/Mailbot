import discord
from discord.ext import commands
import aiohttp
import imgmanip


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def waaw(self, ctx):
        """Mirrors an image from the left side"""
        try:
            imgUrl = ctx.message.attachments[0].url
            async with aiohttp.ClientSession() as session:
                async with session.get(imgUrl) as req:
                    if req.status != 200:
                        await ctx.send("Something went wrong :(")
                    imgData = await req.read()
            workImg = imgmanip.openImg(imgData)
            imgOut = imgmanip.lMirror(workImg)
            await ctx.send(file=discord.File(imgOut))
        except IndexError:
            await ctx.send("Error :( please try again")

    @commands.command()
    async def haah(self, ctx):
        """Mirrors an image from the right side"""
        try:
            imgUrl = ctx.message.attachments[0].url
            async with aiohttp.ClientSession() as session:
                async with session.get(imgUrl) as req:
                    if req.status != 200:
                        await ctx.send("Something went wrong :(")
                    imgData = await req.read()
            workImg = imgmanip.openImg(imgData)
            imgOut = imgmanip.rMirror(workImg)
            await ctx.send(file=discord.File(imgOut))
        except IndexError:
            await ctx.send("Error :( please try again")


def setup(bot):
    bot.add_cog(Images(bot))
