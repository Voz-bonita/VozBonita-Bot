import discord
from discord.ext import commands
import random

class Tapas(commands.Cog):

    @commands.command()
    async def tapanagostosa(self, ctx):

        S_N = ["0","1", "2"]
        T_frase = random.choice(S_N)
        verbo = ["Deu", "Mordeu", "Tentou", "Acariciou", "Gemeu", "Pediu", "Colocou", "Fez", "Cobrou",
                 "Chamou", "Regou", "Cavalgou", "Mostrou", "Dedilhou", "Chupou", "Virou", "Tomou", "Sentiu", "Beijou",
                 "Tocou", "Sussurou", "Descobriu", "Cheirou", "Vomitou", "Lambeu", "Assoprou", "Depilou", "Socou",
                 "Imaginou", "Fodeu com força", "Fumou", "Comeu", "Massageou", "Cutucou", "Decorou", "Cortou",
                 "Esfregou", "Bebeu", "Sugou", "Comprou", "Trancou", "Sequestrou", "Escondeu", "Refrescou", "Assistiu",
                 "Ganhou", "Vendeu", "Entortou", "Trancou", "Respeitou", "Amou", "Mentiu", "Surrupiou", "Verificou",
                 "Amassou", "Chamuscou", "Liquefez", "Fotografou", "Dedurou", "Vazou", "Lingou", "Lambeu", "Metaforou",
                 "Furou", "Triturou"
                 ]

        complemento_V = ["os lábios", "um pau", "o mamilo", "a orelha", "o vizinho", "a flauta", "o clitóris", "de 4",
                         "o alazão", "o micropênis", "a goiabeira", "uma surra", "uma mensagem", "o peão", "uma aranha",
                         "seringas", "o joelho", "o dinheiro", "a bunda", "as axilas", "o pulso", "a coxa", "o pescoço",
                         "o bolso", "o relógio", "alguns pentelhos", "a pulseira", "a tiara", "o brinco", "o pau",
                         "a cobra", "o leite", "a descarga", "o ronco", "o ouvidinho virgem", "o bonecão", "o pé",
                         "o baralho", "o anûs", "a língua", "o olho", "o dedo", "o dedo do pé", "a torta", "o pudim",
                         "o pavê", "o pepino", "o toddynho", "o colar", "o umbigo", "a bola", "uma e-girl",
                         "um pack de fotos da foice tortona pra esquerda", "uma maracutaia", "a lâmpada", "o trabalho",
                         "o curso", "um dindim", "o pirocão", "um tapa"]

        complemento_V_N = complemento_V.copy()
        if str(ctx.guild) == "Voz bonita":
            nomes = ['o José', 'o Lucas', 'o Matheus', 'a Thaissa', 'o Thiago', 'a mãe', 'o pai']
            complemento_N = ['do José', 'do Lucas', 'do Matheus', 'da Thaissa', 'do Thiago', 'da mãe', 'do pai']

        else:
            nomes = ["o Akira", "o Caio", "o João", "o José", "o Matheus", "o Thiago","a Emanoela",
                     "a Thalita", "a Laís", "a Larissa", "a mãe", "o pai"]
            complemento_N = ["do Akira", "do Caio", "do João", "do José", "do Matheus", "do Thiago",
                             "da mãe", "do pai", "da Emanoela", "da Laís", "da Larissa", "da Thalita"]

        complemento_V_N.extend(nomes)




        Lugares = ["na fila do banco", "no mercado", "no Salesiano", "na árvore", "debaixo da mesa",
                   "em cima da mesa", "na biblioteca do Salesiano", "no ParkShopping", "no Domingão do Faustão",
                   "no armário", "no telhado", "no ponto de ônibus", "no Discord",
                   "no RPG", "no chão", "na parede", "na cama", "na cadeira de rodas", "num hospital infantil",
                   "no sofá", "no córrego", "na gaveta", "no banho",
                   "na janela", "na boca de fumo", "no bueiro", "no Parque", "na lama",
                   "num balanço", "num escorregador", "no trepa-trepa", "no porão do Silvio Santos",
                   "na chuva", "numa lanchonete", "no siricutico"
                   ]


        if T_frase == "1":
            rodada = f'{random.choice(verbo)} {random.choice(complemento_V)} {random.choice(complemento_N)}'

        elif T_frase == "2":
            rodada = f'{random.choice(verbo)} {random.choice(complemento_V_N)}'

        else:
            rodada = f'{random.choice(verbo)} {random.choice(complemento_V)}'


        L_OU_NL = random.choice(["0", "1"])
        if L_OU_NL == "1":
            rodada += f' {random.choice(Lugares)}'



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
            "manuh": "Emanoela"
        }
        cores = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]
        mscleave = discord.Embed(
            title=f'{autistas[autor]}\n{rodada} :game_die:',
            color=random.choice(cores)
        )

        await ctx.send(embed=mscleave)


        # embonus = [" :star2:"," :sparkles:", " :zap:"]
        # await message.channel.send(str(sum(bonus)) + random.choice(embonus))
        # await message.channel.send("Você tirou: " + str(total) + random.choice(dano))

    @commands.command()
    async def tapanoakira(self,ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanocaio(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanojoao(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanojose(self, ctx):
        if str(ctx.author) != "José#0237":
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
                "Nero.Naka": "Vitor"
            }
            cores = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]
            adj = ["redondinha", "gorda", "feia", "cabeluda", "gostosa", "magra"]
            mscleave = discord.Embed(
                title=f'Voz bonita\nDeu umas palmadas na bunda {random.choice(adj)} d@ {autistas[autor]} :peach:',
                color=random.choice(cores)
            )

            await ctx.send("Você não pode bater no papai")
            await ctx.send(embed=mscleave)
        else:
            await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanolucas(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanomatheus(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanorafael(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanothiago(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanovitor(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanaemanoela(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanalais(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanalarissa(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanathalita(self, ctx):
        await self.tapanagostosa(ctx)

    @commands.command()
    async def tapanathaissa(self, ctx):
        await self.tapanagostosa(ctx)

def setup(client):
    client.add_cog(Tapas(client))
    print("Luvas prontas!")