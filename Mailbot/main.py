#!/usr/bin/env python
# Mailbot main script

import os
import discord
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

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.owo '):
        await message.channel.send(owo.owo(message.content[5:]))

    elif 'GOODNIGHT RYAN' in message.content.upper():
        await message.channel.send("Goodnight Ryan!")

    elif message.content.startswith('ay'):
        await message.channel.send("I can fly!")

    elif message.content.startswith('.cry '):
        await message.channel.send(cry.cry(message.content[5:]))

    elif message.content.startswith('.crowo '):
        usefulMsg = message.content[7:]
        cryOutput = cry.cry(usefulMsg)
        combOutput = owo.owo(cryOutput)
        await message.channel.send(combOutput)

    elif message.content.startswith('.rps '):
        usefulMsg = message.content[5:].upper()
        playerChoice = rps.inputOption(usefulMsg)
        if playerChoice != None:
            compChoice = rps.compChoice()
            winningCond = rps.calculateWinner(playerChoice, compChoice)
            rpsOutput = rps.finalMessage(playerChoice, compChoice, winningCond)
            await message.channel.send(rpsOutput)
        else:
            await message.channel.send("Input error, please try again.")

    elif message.content.startswith('.yt '):
        usefulMsg = message.content[4:].replace(' ', '%20')
        ytRequest = urllib.request.urlopen(
            "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&type=video&q=" + usefulMsg + "&key=" + youtubeToken).read()
        ytOutput = json.loads(ytRequest)
        await message.channel.send("https://youtube.com/watch?v=" + ytOutput['items'][0]['id']['videoId'])

    elif message.content.startswith('.8ball '):
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
        await message.channel.send(random.choice(ballList))

    elif message.content.startswith('.jerk'):
        comicNum = str(random.randrange(1, 7700))
        await message.channel.send("https://www.bonequest.com/" + comicNum + ".gif")


client.run(discordToken)
