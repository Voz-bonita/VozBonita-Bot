import discord
from discord.ext import commands
from random import choice, randint
from Cogs.Music import colors

# You can add places if you want so
path = "Cogs/Slap_words/"
verbs = open(f"{path}verbs.txt").readline().split(",")
complement = open(f"{path}complement.txt").readline().split(",")
names = open(f"{path}names.txt").readline().split(",")


class Tapas(commands.Cog):

    @commands.command()
    async def tapanagostosa(self, ctx):
        action = choice(verbs) + " "
        possibilities = randint(0, 2)

        actions = {0: choice(complement),
                   1: f"{choice(complement)} d{choice(names)}",
                   2: choice(names)}

        action += actions[possibilities]

        author = ctx.author.display_name
        mscleave = discord.Embed(
            title=f'{author}\n{action} :game_die:',
            color=choice(colors)
        )

        await ctx.send(embed=mscleave)


def setup(client):
    client.add_cog(Tapas(client))
    print("Gloves on!")
