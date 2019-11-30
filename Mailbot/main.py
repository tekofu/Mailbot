#!/usr/bin/env python
# Mailbot main script

import os
import discord
import owotrans
import argparse

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

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(parser.parse_args().input)


