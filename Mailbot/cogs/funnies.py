import random
import aiohttp
import discord
from discord.ext import commands
from cogs.utils import beans, rps
from cogs.utils.strManip import cry, leet, owo


class Funnies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, voice, *text):
        """echos text in different 'voices'. see '.help voices'"""
        voiceChoice = voice.lower().split('+')
        voiceOutput = ' '.join(text)
        if 'owo' in voiceChoice:
            voiceOutput = owo.owo(voiceOutput)
        if 'cry' in voiceChoice:
            voiceOutput = cry.cry(voiceOutput)
        if 'leet' in voiceChoice:
            voiceOutput = leet.leet(voiceOutput)
        if any(x in voiceChoice for x in ['owo', 'cry', 'leet']) == False:
            await ctx.send(f'{voice} {voiceOutput}')
            return
        await ctx.send(voiceOutput)

    @commands.command(name='voices')
    async def voices(self, voice):
        """owo | cry | leet. use + separator to combine"""
        return

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
            await ctx.send('Input error, please try again.')

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
                        await ctx.send('Something went wrong :(')
                    comicIndex = await req.json()

            comicNum = str(random.randrange(
                1, comicIndex['episodes'][0]['episode']))
            await ctx.send(f'https://www.bonequest.com/{comicNum}.gif')
        else:
            query = '+'.join(query)
            async with aiohttp.ClientSession() as session:
                async with session.get('https://bonequest.com/search/?q={query}&json=json') as req:
                    if req.status != 200:
                        await ctx.send('Something went wrong :(')
                    searchIndex = await req.json()

            comicNum = str(searchIndex[0]['episode'])
            await ctx.send(f'https://www.bonequest.com/{comicNum}.gif')

    @commands.command()
    async def cat(self, ctx):
        """Gives you a random cat."""
        async with aiohttp.ClientSession() as session:
            async with session.get('http://aws.random.cat/meow') as req:
                if req.status != 200:
                    await ctx.send('Something went wrong :(')
                reply = await req.json()
                await ctx.send(embed=discord.Embed(title='Look at this random cat!').set_image(url=reply['file']))

    @commands.command()
    async def dog(self, ctx):
        """Gives you a random dog."""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://random.dog/woof?filter=mp4,webm') as req:
                if req.status != 200:
                    await ctx.send('Something went wrong :(')
                filename = await req.text()
                url = f'https://random.dog/{filename}'
            await ctx.send(embed=discord.Embed(title='Look at this random dog!').set_image(url=url))

    @commands.command()
    async def frog(self, ctx):
        """Gives you a random frog tip."""
        async with aiohttp.ClientSession() as session:
            async with session.get('http://frog.tips/api/1/tips') as req:
                if req.status != 200:
                    await ctx.send('Something went wrong :(')
                frogCroak = await req.json()
            frogNum = str(frogCroak['tips'][0]['number'])
            frogTip = frogCroak['tips'][0]['tip']
            await ctx.send(f'**Frog tip #{frogNum}**\n{frogTip}')

    @commands.command(hidden=True)
    async def bean(self, ctx):
        """Gives you a random bean fact"""
        await ctx.send(random.choice(beans.beanList))

    @commands.command(hidden=True)
    async def dril(self, ctx):
        """Gives you a random dril tweet"""
        async with aiohttp.ClientSession() as session:
            async with session.get('https://tekofu.com/dril.json') as req:
                if req.status != 200:
                    await ctx.send('Something went wrong :(')
                drilList = await req.json()

            #print(drilList['urls'])
            drilTweet = drilList['urls'][random.randrange(0, 9854)]
            await ctx.send(drilTweet)

def setup(bot):
    bot.add_cog(Funnies(bot))
