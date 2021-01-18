import discord
import os
from discord.ext import commands
client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('RPG'))
    print('Ligado e melhorado, papai')


@client.command()
async def load(ctx, extension):
    if str(ctx.author) == "José#0237":
        client.load_extension(f'Engrenagens.{extension}')
        await ctx.send("É pra já, papai")

    else:
        await ctx.send("Mamãe?")

@client.command()
async def unload(ctx, extension):
    if str(ctx.author) == "José#0237":
        client.unload_extension(f'Engrenagens.{extension}')
        await ctx.send("É pra já, papai")

    else:
        await ctx.send("Mamãe?")

@client.command()
async def reload(ctx, extension):
    if str(ctx.author) == "José#0237":
        client.unload_extension(f'Engrenagens.{extension}')
        client.load_extension(f'Engrenagens.{extension}')
        await ctx.send("É pra já, papai")

    else:
        await ctx.send("Mamãe?")


for arquivo in os.listdir("./Engrenagens"):
    if arquivo.endswith(".py"):
        client.load_extension(f'Engrenagens.{arquivo[:-3]}')

client.run(os.environ["TOKEN"])