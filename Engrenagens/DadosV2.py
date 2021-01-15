import discord
from discord.ext import commands
import random

class DadosV2(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self,ctx,*,dados):
        rolagem = []

        dados = dados.split()
        if not isinstance(dados, str):
            for i in range(0,len(dados),2):
                rolagem.append(dados[i])
        else:
            rolagem.append(dados)

        resultado = []
        for roll in rolagem:
            if 'd' in roll:
                soma = 0
                qnt, dado = map(int,roll.split('d'))
                for i in range(qnt):
                    soma += random.randint(1,dado)

                resultado.append(soma)
            else:
                resultado.append(roll)

        exp = ''
        for i in range(len(dados)):
            if i%2 == 0:

                exp += str(resultado[i//2])
            else:
                exp += dados[i]

        autor = str(ctx.author)
        autor = autor[:-5]
        autistas = {
            "cobrador73": "Matheus",
            "Schezo, The Dark Mage": "Gabriel",
            "JP33": "João Pedro",
            "Rafalula": "Rafael",
            "DryiaKitsune": "Thaissa",
            "Ishida Maki": "Thiago",
            "Gordon2": "Victor",
            "Snorcs": "José",
            "José": "José",
            "Rafa": "Rafael",
            "ArtherKobenh": "Gabriel",
            "lucaskywalker": "Lucas",
            "🎲NINA🎲": "NINA",
            "karolxp": "Karol",
            "Не бойтесь": "Thiago",
            "Akira": "Akira",
            "Thalitinha gameplays": "Thalita",
            "lari": "Larissa",
            "Lala": "Laís",
            "Emanoela15": "Emanoela",
            "Naomi-kun (＃ ＞ ＜)": "Matheus",
            "llari2.0": "Larissa",
            "Lima May": "João",
            "Satan": "João",
            "Caiozera": "Caio",
            "manuh": "Emanoela",
            "JoaoPedroBot": "João Pedro"
        }
        cores = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]

        mscleave = discord.Embed(
            title=f'{autistas[autor]}\nGot {eval(exp)} :game_die:',
            color=random.choice(cores)
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
    client.add_cog(DadosV2(client))
    print("Dados presentes!")