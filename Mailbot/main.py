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

tokenFile = open("tokens.json", "r")
tokenLoad = json.load(tokenFile)
discordToken = tokenLoad['discordToken']
youtubeToken = tokenLoad['youtubeToken']
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


bot = Mailbot(command_prefix='.', description=description)


@bot.command(name='owo', description='owo-ify the text')
async def owoCom(ctx, *, text):
    await ctx.send(owo.owo(text))


@bot.command(name='cry', description='cry-ify the text')
async def cryCom(ctx, *, text):
    await ctx.send(cry.cry(text))


@bot.command(description='owo *and* cry-ify the text')
async def crowo(ctx, *, text):
    cryOutput = cry.cry(text)
    combOutput = owo.owo(cryOutput)
    await ctx.send(cry.cry(combOutput))


@bot.command(name='rps', description='Play Rock paper scissors with the bot')
async def rpsCom(ctx, choice):
    usefulMsg = choice.upper()
    playerChoice = rps.inputOption(usefulMsg)
    if playerChoice != None:
        compChoice = rps.compChoice()
        winningCond = rps.calculateWinner(playerChoice, compChoice)
        rpsOutput = rps.finalMessage(playerChoice, compChoice, winningCond)
        await ctx.send(rpsOutput)
    else:
        await ctx.send("Input error, please try again.")


@bot.command(name='8ball', description='Ask the bot a Magic 8-Ball question')
async def eightBall(ctx, *, question):
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


@bot.command(description='Posts a random Bonequest comic')
async def jerk(ctx):
    comicNum = str(random.randrange(1, 7700))
    await ctx.send("https://www.bonequest.com/" + comicNum + ".gif")


@bot.command(description='Searches YouTube and posts the first result')
async def yt(ctx, *, query):
    usefulMsg = query.replace(' ', '%20')
    ytRequest = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&type=video&q=" + usefulMsg + "&key=" + youtubeToken).read()
    ytOutput = json.loads(ytRequest)
    await ctx.send("https://youtube.com/watch?v=" + ytOutput['items'][0]['id']['videoId'])


bot.run(discordToken)
