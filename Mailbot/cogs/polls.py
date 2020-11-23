#import json
import discord
from discord.ext import commands

#resultsFile = open('polls.json')
#resultsLoad = json.load(resultsFile)

emojiList = [
    '1️⃣',
    '2️⃣',
    '3️⃣',
    '4️⃣'
]


class Polling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, *, args):
        """Adds a new poll to be voted on"""
        pollCat = 'uncategorised'
        pollOptions = list()
        maxOptions = 4

        if args.find('+') != -1:
            pollCat = args[0:args.find(' ')]
            args = args[args.find(' '):len(args)]

        titleStart = args.find('{') + 1
        titleEnd = args.find('}')
        pollTitle = args[titleStart:titleEnd]
        args = args[titleEnd:len(args)]

        while maxOptions > 0:
            optionStart = args.find('[') + 1
            optionEnd = args.find(']')
            if args[optionStart:optionEnd] == '':
                break
            pollOptions.append(args[optionStart:optionEnd])
            args = args[optionEnd + 1:len(args)]
            maxOptions = maxOptions - 1

        pollBody = ''

        for x in range(len(pollOptions)):
            pollBody += str(x + 1) + '. ' + pollOptions[x] + '\n'

        pollInfo = f'New **{pollCat}** poll ready to vote on!'

        embed = discord.Embed(title=pollTitle, description=pollBody)

        pollPost = await ctx.send(embed=embed, content=pollInfo)

        for x in range(len(pollOptions)):
            await pollPost.add_reaction(emojiList[x])


def setup(bot):
    bot.add_cog(Polling(bot))
