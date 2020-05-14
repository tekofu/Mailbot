#!/usr/bin/env python
# Mailbot main script

import json
import discord
from discord.ext import commands
from cogs import funnies, images, utilities

tokenFile = open('config.json', 'r')
tokenLoad = json.load(tokenFile)
discordToken = tokenLoad['discordToken']
youtubeToken = tokenLoad['youtubeToken']
boardId = int(tokenLoad['starboardId'])
description = 'A bad discord robot for the Mailroom'


class Mailbot(commands.Bot):
    async def on_ready(self):
        print('Now logged in as {0.user}'.format(bot))
        await bot.change_presence(activity=discord.Activity(name='you sleep', type=discord.ActivityType.watching))
        funnies.setup(self)
        images.setup(self)
        utilities.setup(self)

    async def on_message(self, message):
        if message.author == bot.user:
            return

        elif 'GOODNIGHT RYAN' in message.content.upper():
            await message.channel.send('Goodnight Ryan!')

        elif message.content.startswith('ay'):
            await message.channel.send('I can fly!')

        await bot.process_commands(message)

    async def on_raw_reaction_add(self, payload):
        starEmoji = '\N{WHITE MEDIUM STAR}'

        if str(payload.emoji) != starEmoji:
            return

        channel = bot.get_channel(payload.channel_id)
        starMessage = await channel.fetch_message(payload.message_id)

        msgReactions = starMessage.reactions

        for reaction in msgReactions:
            if reaction.emoji == starEmoji:
                starCount = reaction.count

        if starCount != 1:
            return

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

        boardChannel = bot.get_channel(boardId)

        await boardChannel.send(embed=embed)


bot = Mailbot(command_prefix='.', description=description)

bot.run(discordToken)
