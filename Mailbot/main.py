#!/usr/bin/env python
# Mailbot main script

import os
import discord
from discord.ext import commands
import argparse
import urllib.request
import json
import rps
import owo
import cry
import random

tokenFile = open("config.json", "r")
tokenLoad = json.load(tokenFile)
discordToken = tokenLoad['discordToken']
youtubeToken = tokenLoad['youtubeToken']
boardId = int(tokenLoad['starboardId'])
description = 'A bad discord robot for the Mailroom'


class Mailbot(commands.Bot):
    async def on_ready(self):
        print('Now logged in as {0.user}'.format(bot))

    async def on_message(self, message):
        if message.author == bot.user:
            return

        elif 'GOODNIGHT RYAN' in message.content.upper():
            await message.channel.send("Goodnight Ryan!")

        elif message.content.startswith('ay'):
            await message.channel.send("I can fly!")

        await bot.process_commands(message)

    async def on_raw_reaction_add(self, payload):
        starEmoji = '\N{WHITE MEDIUM STAR}'

        if str(payload.emoji) != starEmoji:
            return

        channel = bot.get_channel(payload.channel_id)

        starMessage = await channel.fetch_message(payload.message_id)

        embed = discord.Embed(description=starMessage.content)
        if starMessage.embeds:
            data = starMessage.embeds[0]
            if data.type == 'image':
                embed.set_image(url=data.url)

        if starMessage.attachments:
            file = starMessage.attachments[0]
            if file.url.lower().endswith(('png', 'jpeg', 'jpg', 'gif', 'webp')):
                embed.set_image(url=file.url)
            else:
                embed.add_field(
                    name='Attachment', value=f'[{file.filename}]({file.url})', inline=False)

        embed.add_field(name='Original',
                        value=f'[Jump!]({starMessage.jump_url})', inline=False)
        embed.set_author(name=starMessage.author.display_name,
                         icon_url=starMessage.author.avatar_url_as(format='png'))
        embed.timestamp = starMessage.created_at

        channel = bot.get_channel(boardId)
        await channel.send(embed=embed)


bot = Mailbot(command_prefix='.', description=description)


@bot.command(name='owo')
async def owoCom(ctx, *, text):
    """owo-ify the text"""
    await ctx.send(owo.owo(text))


@bot.command(name='cry')
async def cryCom(ctx, *, text):
    """cry-ify the text"""
    await ctx.send(cry.cry(text))


@bot.command()
async def crowo(ctx, *, text):
    """owo and cry-ify the text"""
    cryOutput = cry.cry(text)
    combOutput = owo.owo(cryOutput)
    await ctx.send(cry.cry(combOutput))


@bot.command()
async def roll(ctx, dice: str):
    """Roll a dice in the format NdN"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def choose(ctx, *choices: str):
    """Choose between multiple options, separated with spaces"""
    await ctx.send(random.choice(choices))


@bot.command(name='rps')
async def rpsCom(ctx, choice):
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


@bot.command(name='8ball')
async def eightBall(ctx, *, question):
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


@bot.command()
async def jerk(ctx):
    """Posts a random Bonequest comic"""
    comicNum = str(random.randrange(1, 7700))
    await ctx.send("https://www.bonequest.com/" + comicNum + ".gif")


@bot.command()
async def yt(ctx, *, query):
    """Searches YouTube and posts the first result"""
    usefulMsg = query.replace(' ', '%20')
    ytRequest = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&type=video&q=" + usefulMsg + "&key=" + youtubeToken).read()
    ytOutput = json.loads(ytRequest)
    await ctx.send("https://youtube.com/watch?v=" + ytOutput['items'][0]['id']['videoId'])


bot.run(discordToken)
