import discord
from discord.ext import commands
import random
import owo
import cry
import rps
import aiohttp


class Funnies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='owo')
    async def owoCom(self, ctx, *, text):
        """owo-ify the text"""
        await ctx.send(owo.owo(text))

    @commands.command(name='cry')
    async def cryCom(self, ctx, *, text):
        """cry-ify the text"""
        await ctx.send(cry.cry(text))

    @commands.command()
    async def crowo(self, ctx, *, text):
        """owo and cry-ify the text"""
        cryOutput = cry.cry(text)
        combOutput = owo.owo(cryOutput)
        await ctx.send(cry.cry(combOutput))

    @commands.command()
    async def roll(self, ctx, dice: str):
        """Roll a dice in the format NdN"""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def choose(self, ctx, *choices: str):
        """Choose between multiple options, separated with spaces"""
        await ctx.send(random.choice(choices))

    @commands.command(name='rps')
    async def rpsCom(self, ctx, choice):
        """Play Rock paper scissors with the bot"""
        usefulMsg = choice.upper()
        playerChoice = rps.inputOption(usefulMsg)
        if playerChoice != None:
            compChoice = rps.compChoice()
            winningCond = rps.calculateWinner(playerChoice, compChoice)
            rpsOutput = rps.finalMessage(playerChoice, compChoice, winningCond)
            await ctx.send(rpsOutput)
        else:
            await ctx.send("Input error, please try again.")

    @commands.command(name='8ball')
    async def eightBall(self, ctx, *, question):
        """Ask the bot a Magic 8-Ball question"""
        ballList = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes – definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.'
        ]
        await ctx.send(random.choice(ballList))

    @commands.command()
    async def jerk(self, ctx, *query):
        """Posts a random or searched for Bonequest comic"""
        if len(query) == 0:
            async with aiohttp.ClientSession() as session:
                async with session.get('https://bonequest.com/index.json') as req:
                    if req.status != 200:
                        await ctx.send("Something went wrong :(")
                    comicIndex = await req.json()

            comicNum = str(random.randrange(
                1, comicIndex['episodes'][0]['episode']))
            await ctx.send("https://www.bonequest.com/" + comicNum + ".gif")
        else:
            query = '+'.join(query)
            async with aiohttp.ClientSession() as session:
                async with session.get('https://bonequest.com/search/?q=' + query + '&json=json') as req:
                    if req.status != 200:
                        await ctx.send("Something went wrong :(")
                    searchIndex = await req.json()

            comicNum = str(searchIndex[0]['episode'])
            await ctx.send("https://www.bonequest.com/" + comicNum + ".gif")

    @commands.command()
    async def cat(self, ctx):
        """Gives you a random cat."""
        async with aiohttp.ClientSession() as session:
            async with session.get('http://aws.random.cat/meow') as req:
                if req.status != 200:
                    await ctx.send("Something went wrong :(")
                reply = await req.json()
                await ctx.send(embed=discord.Embed(title='Look at this random cat!').set_image(url=reply['file']))

    @commands.command()
    async def dog(self, ctx):
        """Gives you a random dog."""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://random.dog/woof?filter=mp4,webm') as req:
                if req.status != 200:
                    await ctx.send("Something went wrong :(")
                filename = await req.text()
                url = f'https://random.dog/{filename}'
            await ctx.send(embed=discord.Embed(title='Look at this random dog!').set_image(url=url))

    @commands.command()
    async def frog(self, ctx):
        """Gives you a random frog tip."""
        async with aiohttp.ClientSession() as session:
            async with session.get('http://frog.tips/api/1/tips') as req:
                if req.status != 200:
                    await ctx.send("Something went wrong :(")
                frogCroak = await req.json()
            frogNum = str(frogCroak['tips'][0]['number'])
            frogTip = frogCroak['tips'][0]['tip']
            await ctx.send('**Frog tip #' + frogNum + '**' + '\n' + frogTip)


def setup(bot):
    bot.add_cog(Funnies(bot))