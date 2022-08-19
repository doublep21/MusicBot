#!/usr/bin/env python3

from discord.utils import get
import discord
import asyncio


client = discord.Client()
TOKEN = "token here"

@client.event
async def on_ready():
  print('Bot is up and running.')
  print(f'Logged in as {client.user}')

@client.event
async def on_message(message, *ctx):
    for guild in client.guilds:
        discord_guild = client.get_guild(int(guild.id))
        link = await discord_guild.text_channels[0].create_invite()
        print(link)
        asyncio.sleep(750)

client.run(TOKEN)
