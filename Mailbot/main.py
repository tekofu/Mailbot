#!/usr/bin/env python
# Mailbot main script

import os
import discord
import argparse
import urllib.request
import json
import rps
import owo

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

    elif message.content.startswith('.cry '):
        usefulMsg = message.content[5:].replace(' ', '%20')
        cryRequest = urllib.request.urlopen(
            "https://api.apcry.deadbird.dev/cry/" + usefulMsg).read()
        cryOutput = json.loads(cryRequest)
        await message.channel.send(cryOutput['tears'])

    elif message.content.startswith('.crowo '):
        usefulMsg = message.content[7:].replace(' ', '%20')
        cryRequest = urllib.request.urlopen(
            "https://api.apcry.deadbird.dev/cry/" + usefulMsg).read()
        cryOutput = json.loads(cryRequest)
        combOutput = owo.owo(cryOutput['tears'])
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


client.run(discordToken)
