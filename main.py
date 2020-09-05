#!/usr/bin/env/str python3

from time import sleep
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
global message_counter
import random

with open("tokenfile", "r") as tokenfile:
    token=tokenfile.read()

my_id = 472465416019771392
client = discord.Client()

@client.event
async def on_ready():
    print('hello world')

generalcooldown = 0
@client.event
async def on_message(message):

    armour = discord.utils.get(message.guild.roles, id = 751637329088610365)
    
    #pant armour
    if message.content.startswith("Pant unarmor"):
        await message.author.remove_roles(armour, reason="armoured")
        await message.channel.send("you are no longer armoured")
        generalcooldown = 1
        await asyncio.sleep(10)
        generalcooldown = 0
    if armour in message.author.roles:
        return
    if message.content.startswith("Pant armor"):
        if generalcooldown == 1:
            return
        await message.author.add_roles(armour, reason="armoured")
        await message.channel.send("you are now armoured")



client.run(token)