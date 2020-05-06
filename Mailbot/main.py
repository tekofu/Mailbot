#!/usr/bin/env python
# Mailbot main script

import os
import discord
from discord.ext import commands
import urllib.request
import json
import funnies


tokenFile = open("config.json", "r")
tokenLoad = json.load(tokenFile)
discordToken = tokenLoad['discordToken']
youtubeToken = tokenLoad['youtubeToken']
boardId = int(tokenLoad['starboardId'])
description = 'A bad discord robot for the Mailroom'


class Mailbot(commands.Bot):
    async def on_ready(self):
        print('Now logged in as {0.user}'.format(bot))
        funnies.setup(self)
        self.starCache = []

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

        if str(payload.message_id) in self.starCache:
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
        self.starCache.append(str(payload.message_id))

        if len(self.starCache) == 20:
            self.starCache.pop(0)

        await channel.send(embed=embed)


bot = Mailbot(command_prefix='.', description=description)


@bot.command()
async def yt(ctx, *, query):
    """Searches YouTube and posts the first result"""
    usefulMsg = query.replace(' ', '%20')
    ytRequest = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&type=video&q=" + usefulMsg + "&key=" + youtubeToken).read()
    ytOutput = json.loads(ytRequest)
    await ctx.send("https://youtube.com/watch?v=" + ytOutput['items'][0]['id']['videoId'])


bot.run(discordToken)
