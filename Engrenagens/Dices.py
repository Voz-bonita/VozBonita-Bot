import discord
from discord.ext import commands
import random


class Dices(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self, ctx, *, dices):
        rolled = []

        dices = dices.split()
        if not isinstance(dices, str):
            # Skips the operators
            for non_op in range(0, len(dices), 2):
                rolled.append(dices[non_op])
        else:
            rolled.append(dices)

        result = []
        for roll in rolled:
            # Check if its a dice
            if 'd' in roll:
                qnt, sides = map(int, roll.split('d'))
                got = random.choices(range(1, sides), k=qnt)
                result.append(sum(got))
                # TODO possibility of showing at Discord every individual dice result
            else:
                result.append(roll)

        exp = ''
        # Odd slots are operators
        # Even slots are dices
        for i in range(len(dices)):
            if i % 2 == 0:
                exp += str(result[i//2])

            else:
                exp += dices[i]

        author = ctx.author.display_name
        colors = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]

        mscleave = discord.Embed(
            title=f'{author}\nGot {eval(exp)} :game_die:',
            color=random.choice(colors)
        )

        await ctx.send(embed=mscleave)

    @commands.command()
    async def calc(self, ctx, exp):
        cores = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]

        mscleave = discord.Embed(
            title=f'{eval(exp)}',
            color=random.choice(cores)
        )

        await ctx.send(embed=mscleave)


def setup(client):
    client.add_cog(Dices(client))
    print("Dices ready!")
