import discord
import os
from discord.ext import commands
client = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('RPG'))
    print('Online and ready!')


@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')
    await ctx.send(f"Cog {extension} loaded")


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    await ctx.send(f"Cog {extension} unloaded")


@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    client.load_extension(f'Cogs.{extension}')
    await ctx.send(f"Cog {extension} reloaded")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I didn't understand")

    elif isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send("I'm not connected to any voice channel :worried:")

for file in os.listdir("./Cogs"):
    if file.endswith(".py"):
        client.load_extension(f'Cogs.{file[:-3]}')

client.run(os.environ["TOKEN"])
