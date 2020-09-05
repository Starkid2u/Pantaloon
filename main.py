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

my_id = 312292633978339329
client = discord.Client()

@client.event
async def on_ready():
    print('hello world')

generalcooldown = 0
pockectcooldown = 0
@client.event
async def on_message(message):

    pocket = discord.utils.get(message.guild.roles, id = 751643312066396181)
    armour = discord.utils.get(message.guild.roles, id = 751637329088610365)
    
    if message.author.id != my_id:
        return

    #pant armour
    global generalcooldown
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

    #pant pocket
    global pockectcooldown
    if message.content.startswith("Pant pocket"):
        print("entering pocket")
        if generalcooldown == 1 or pockectcooldown == 1:
            return
        await message.author.add_roles(pocket, reason="pocketed")
        if not message.mentions == []:
            await message.mentions[0].add_roles(pocket, reason="pocketed")
        pockectcooldown = 1
        await asyncio.sleep(10)
        pockectcooldown = 0
    if message.content.startswith("Pant unpocket"):
        print("exiting pocket")
        if generalcooldown == 1:
            return
        await message.author.remove_roles(pocket, reason="unpocketed")
        if not message.mentions == []:
            await message.mentions[0].remove_roles(pocket, reason="unpocketed")
        if not pocket.members == []:
            personleave = random.randrange(1, 100, 1)
            if personleave in range(1, 25):
                escapee = pocket.members[random.randint(0,len(pocket.members) - 1)]
                print(f"{escapee} escaped the pocket!")
                await escapee.remove_roles(pocket, reason="escaped")



client.run(token)