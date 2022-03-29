import aiohttp
import json
import discord

from discord.ext import commands

tokenFile = open('config.json')
tokenLoad = json.load(tokenFile)
xivKey = '&private_key=[' + tokenLoad['xivToken']


class XIVAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def market(self, ctx, *, query):
        """Shows listings for an item from the Marketboard"""
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://xivapi.com/search?string={query}&indexes=Item&limit=1') as req:
                if req.status != 200:
                    await ctx.send('Something went wrong :(')
                itemDump = await req.json()

        if itemDump["Results"] == 0:
            await ctx.send(f'No results found for {query}')
        else:
            itemID = itemDump["Results"][0]["ID"]
            itemName = itemDump["Results"][0]["Name"]
            itemIcon = itemDump["Results"][0]["Icon"]

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://universalis.app/api/Light/{itemID}?&listings=5') as req:
                if req.status != 200:
                    await ctx.send('Something went wrong :(')
                marketDump = await req.json()

        embed = discord.Embed()
        embed.add_field(name='Universalis Link:',
                        value=f'https://universalis.app/market/({itemID})', inline=False)
        embed.set_author(name=itemName,
                         icon_url='https://xivapi.com/' + itemIcon)

        for listing in marketDump["listings"]:
            embed.add_field(
                name=listing["worldName"],
                value=str(listing["quantity"]) + ' selling at ' +
                str(listing["pricePerUnit"]) + ' gil.',
                inline=False
            )

        await ctx.send(embed=embed)

    @commands.command()
    async def char(self, ctx, forename, surname, world):
        """Searches for a character on the Lodestone"""
        charRequest = f'{forename} {surname}'

        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://xivapi.com/character/search?name=\
                {charRequest}&server={world}') as req:
                if req.status != 200:
                    await ctx.send('Something went wrong :(')
                character = await req.json()

        embed = discord.Embed(description='on ' +
                              character['Results'][0]['Server'])
        embed.set_image(url=character['Results'][0]['Avatar'])

        lodestoneURL = 'https://eu.finalfantasyxiv.com/lodestone/character/' + \
            str(character['Results'][0]['ID'])

        embed.add_field(name='Lodestone',
                        value=f'[Profile]({lodestoneURL})', inline=False)
        embed.set_author(name=character['Results'][0]['Name'],
                         icon_url=character['Results'][0]['Avatar'])

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(XIVAPI(bot))
