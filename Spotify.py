import discord
from discord.ext import commands
import requests
import threading
import asyncio
import urllib.request
from urllib.request import Request, urlopen
import json
import getpass
from colorama import Fore, Style
import os, time, datetime, random, asyncio, aiohttp, json, discord, time, colorama, requests
from itertools import cycle
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
import pyfiglet
from pyfiglet import Figlet
from discord.utils import get
import time
import string

client = commands.Bot(command_prefix='!', case_insensitive=True)
client.remove_command('help')

Codes = "codes.txt"



@client.event
async def on_ready():
    print('SpotifyUpgrader Is Ready')
    await client.change_presence(activity=discord.Game(name='All Hail warsnoop#0755'))
    try:
        with open(Codes, "r") as file:
            client.codes = [code.strip("\n") for code in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"{Codes} doesn't exist.")

@client.command()
async def Donate(ctx):
    embed = discord.Embed(title="Spotify Upgrader", color=0x03fc14)
    embed.add_field(name=f"LTC:", value=(f'LXxWtHoDuNmEvjaY9ZYCBQF1ooecJT9F9L'), inline=False)
    embed.add_field(name=f"BTC:", value=(f'Not set yet'), inline=False)
    embed.add_field(name=f"warsnoop#0755", value=(f'Developed by warsnoop#0755 Feel Free to add me!'), inline=False)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def Gen(ctx, codes: int):
    f = open('codes.txt', 'a')
    gay = 0
    while gay <= codes:
        x = ('').join(random.choices(string.ascii_letters + string.digits, k=40))
        f.write(x + '\n')
        gay += 1
    await ctx.send('Done generating codes')

@client.command()
async def Redeem(ctx, code: str, country: str):
    if code not in client.codes:
        embed = discord.Embed(title="Spotify Upgrader", color=0xfc1c03)
        embed.add_field(name=f"Error", value=('Wrong key!'), inline=False)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        with open(Codes, "r") as file:
            client.codes = [code.strip("\n") for code in file.readlines()]
    else:
        embed = discord.Embed(title="Spotify Upgrader", color=0x03fc14)
        embed.add_field(name=f"Success", value=(f'SuccessFully Reedemed Key for {country}!'), inline=False)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

        with open(f"{country}.txt", "r") as file2:
            x = file2.readline()
            Invite = x.split(':')[0]
            Address = x.split(':')[1]
        

        embed = discord.Embed(title="Spotify Upgrader", color=0x03fc14)
        embed.add_field(name=f"{Invite}", value=(Address), inline=False)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.author.send(embed=embed)

        with open(f"{country}.txt", "r") as file_input:
            with open(f"{country}.txt", "w") as output: 
                for line in file_input:
                    if line.strip("\n") != f"{x}":
                        output.write(line)

        client.codes.remove(code)
        with open("codes.txt", "a") as file:
            file.truncate(0)
            for code in client.codes:
                file.write(f"{code}\n")




@client.command(pass_context=True)
async def stock(ctx):
    embed = discord.Embed(title="Spotify Upgrader", color=0xfc0a4f)
    num_lines = sum(1 for line in open('AR.txt'))
    num_lines2 = sum(1 for line in open('AT.txt'))
    num_lines3 = sum(1 for line in open('AU.txt'))
    num_lines4 = sum(1 for line in open('BR.txt'))
    num_lines5 = sum(1 for line in open('CA.txt'))
    num_lines6 = sum(1 for line in open('CH.txt'))
    num_lines7 = sum(1 for line in open('CL.txt'))
    num_lines8 = sum(1 for line in open('CO.txt'))
    num_lines9 = sum(1 for line in open('CR.txt'))
    num_lines10 = sum(1 for line in open('CZ.txt'))
    num_lines11 = sum(1 for line in open('DE.txt'))
    num_lines12 = sum(1 for line in open('DK.txt'))
    num_lines13 = sum(1 for line in open('DO.txt'))
    num_lines14 = sum(1 for line in open('EC.txt'))
    num_lines15 = sum(1 for line in open('ES.txt'))
    num_lines16 = sum(1 for line in open('Fl.txt'))
    num_lines17 = sum(1 for line in open('GB.txt'))
    num_lines18 = sum(1 for line in open('HK.txt'))
    num_lines19 = sum(1 for line in open('HN.txt'))
    num_lines20 = sum(1 for line in open('HU.txt'))
    num_lines21 = sum(1 for line in open('ID.txt'))
    num_lines22 = sum(1 for line in open('IE.txt'))
    num_lines23 = sum(1 for line in open('IS.txt'))
    num_lines24 = sum(1 for line in open('IT.txt'))
    num_lines25 = sum(1 for line in open('MX.txt'))
    num_lines26 = sum(1 for line in open('NL.txt'))
    num_lines27 = sum(1 for line in open('NO.txt'))
    num_lines28 = sum(1 for line in open('NZ.txt'))
    num_lines29 = sum(1 for line in open('PH.txt'))
    num_lines30 = sum(1 for line in open('SE.txt'))
    num_lines31 = sum(1 for line in open('SG.txt'))
    num_lines32 = sum(1 for line in open('TH.txt'))
    num_lines33 = sum(1 for line in open('TR.txt'))
    num_lines34 = sum(1 for line in open('US.txt'))
    embed.add_field(name=f"AR:",value=str(num_lines), inline=False)
    embed.add_field(name=f"AT:",value=str(num_lines2), inline=False)
    embed.add_field(name=f"AU:",value=str(num_lines3), inline=False)
    embed.add_field(name=f"BR:",value=str(num_lines4), inline=False)
    embed.add_field(name=f"CA:",value=str(num_lines5), inline=False)
    embed.add_field(name=f"CH:",value=str(num_lines6), inline=False)
    embed.add_field(name=f"CL:",value=str(num_lines7), inline=False)
    embed.add_field(name=f"CO:",value=str(num_lines8), inline=False)
    embed.add_field(name=f"CR:",value=str(num_lines9), inline=False)
    embed.add_field(name=f"CZ:",value=str(num_lines10), inline=False)
    embed.add_field(name=f"DE:",value=str(num_lines11), inline=False)
    embed.add_field(name=f"DK:",value=str(num_lines12), inline=False)
    embed.add_field(name=f"DO:",value=str(num_lines13), inline=False)
    embed.add_field(name=f"EC:",value=str(num_lines14), inline=False)
    embed.add_field(name=f"ES:",value=str(num_lines15), inline=False)
    embed.add_field(name=f"FL:",value=str(num_lines16), inline=False)
    embed.add_field(name=f"GB:",value=str(num_lines17), inline=False)
    embed.add_field(name=f"HK:",value=str(num_lines18), inline=False)
    embed.add_field(name=f"HN:",value=str(num_lines19), inline=False)
    embed.add_field(name=f"HU:",value=str(num_lines20), inline=False)
    embed.add_field(name=f"ID:",value=str(num_lines21), inline=False)
    embed.add_field(name=f"IE:",value=str(num_lines22), inline=False)
    embed.add_field(name=f"IS:",value=str(num_lines23), inline=False)
    embed.add_field(name=f"IT:",value=str(num_lines24), inline=False)
    embed.add_field(name=f"MX:",value=str(num_lines25), inline=False)
    embed.add_field(name=f"NL:",value=str(num_lines26), inline=False)
    embed.add_field(name=f"NO:",value=str(num_lines27), inline=False)
    embed.add_field(name=f"NZ:",value=str(num_lines28), inline=False)
    embed.add_field(name=f"PH:",value=str(num_lines29), inline=False)
    embed.add_field(name=f"SE:",value=str(num_lines30), inline=False)
    embed.add_field(name=f"sg:",value=str(num_lines31), inline=False)
    embed.add_field(name=f"TH:",value=str(num_lines32), inline=False)
    embed.add_field(name=f"TR:",value=str(num_lines33), inline=False)
    embed.add_field(name=f"US:",value=str(num_lines34), inline=False)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="SpotifyUpgrader", color=0xfc0a4f)
    embed.add_field(name=f"!Stock", value='Shows the stock!', inline=False)
    embed.add_field(name=f"!Redeem (code) (country)",value='Reedems the key and send you DM!', inline=False)
    embed.add_field(name=f"!Donate",value='Donate warsnoop (owner of the bot)!', inline=False)
    embed.add_field(name=f"!Gen (number)",value='Generated number of codes! (Admin only)', inline=False)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

client.run('ODQ4NDQ2NjE5MDQwODc0NDk2.YLMvfQ.f2b8uM2GtFSr93DlzYy9UW6FS0Q')