#!/usr/bin/env python
# Mailbot main script

import os
import discord
from owotrans import owo
import argparse
import urllib.request
import json

parser = argparse.ArgumentParser()
parser.add_argument("token", help="Discord bot token.")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.owo '):
        await message.channel.send(owo(message.content[4:]))

    # uhhh
    #elif message.content.upper.startswith('GOODNIGHT RYAN'):
    #   await message.channel.send("Goodnight Ryan!")

    elif message.content.startswith('.cry '):
        usefulMsg = message.content[5:].replace(' ', '%20')
        cryRequest = urllib.request.urlopen("https://api.apcry.deadbird.dev/cry/" + usefulMsg).read()
        cryOutput = json.loads(cryRequest)
        await message.channel.send(cryOutput['tears'])

client.run(parser.parse_args().token)


