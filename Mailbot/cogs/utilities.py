import discord
from discord.ext import commands
import aiohttp
import json


tokenFile = open("config.json", "r")
tokenLoad = json.load(tokenFile)
youtubeToken = tokenLoad['youtubeToken']


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yt(self, ctx, *, query):
        """Searches YouTube and posts the first result"""
        usefulMsg = query.replace(' ', '%20')
        async with aiohttp.ClientSession() as session:
            async with session.get(
                'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&type=video&q=' +
                    usefulMsg + '&key=' + youtubeToken) as req:
                if req.status != 200:
                    await ctx.send("Something went wrong :(")
                ytOutput = await req.json()

        await ctx.send("https://youtube.com/watch?v=" + ytOutput['items'][0]['id']['videoId'])

    @commands.command()
    async def wiki(self, ctx, *, query):
        """Searches Wikipedia and posts the first result"""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                'https://en.wikipedia.org/w/api.php?action=opensearch&search=' +
                    query + '&limit=1&namespace=0&format=json') as req:
                if req.status != 200:
                    await ctx.send("Something went wrong :(")
                wikiOutput = await req.json()
        try:
            await ctx.send(wikiOutput[3][0])
        except IndexError:
            await ctx.send('Sorry! No article found')


def setup(bot):
    bot.add_cog(Utilities(bot))
