import json
import aiohttp
import discord
from discord.ext import commands

tokenFile = open('config.json')
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
                f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&type=video&q= \
                    {usefulMsg}&key={youtubeToken}') as req:
                if req.status != 200:
                    await ctx.send('Something went wrong :(')
                ytOutput = await req.json()

        await ctx.send('https://youtube.com/watch?v=' + ytOutput['items'][0]['id']['videoId'])

    @commands.command()
    async def wiki(self, ctx, *, query):
        """Searches Wikipedia and posts the first result"""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f'https://en.wikipedia.org/w/api.php?action=opensearch&search={query} \
                    &limit=1&namespace=0&format=json') as req:
                if req.status != 200:
                    await ctx.send('Something went wrong :(')
                wikiOutput = await req.json()
        try:
            await ctx.send(wikiOutput[3][0])
        except IndexError:
            await ctx.send('Sorry! No article found')

    @commands.command()
    async def ud(self, ctx, *, query):
        """Get a definition of a term from Urban Dictionary"""
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'http://urbanscraper.herokuapp.com/define/{query}') as req:
                if req.status == 404:
                    await ctx.send(f'No definition found for "{query}"')
                elif req.status != 200:
                    await ctx.send('Something went wrong :(')
                udOutput = await req.json()

        embed = discord.Embed()

        embed.add_field(name=query, value=udOutput['definition'])
        try:
            await ctx.send(embed=embed)
        except IndexError:
            await ctx.send('Sorry! No definition found')


def setup(bot):
    bot.add_cog(Utilities(bot))
