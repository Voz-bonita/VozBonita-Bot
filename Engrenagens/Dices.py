import discord
from discord.ext import commands
import random

class Dados(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def legacyroll(self, ctx, *, rolagens):
        total = 0
        quantidade_de_mais = 0
        dados = []
        bonus = []
        rolagens = rolagens.split()
        #mensagem_separada.remove("/roll")

        if "+" in rolagens:
            for i in range(len(rolagens)):
                if rolagens[i] == "+":
                    quantidade_de_mais += 1
            for i in range(quantidade_de_mais):
                rolagens.remove("+")

        for rolagem in rolagens:
            if "d" in rolagem:
                dado = rolagem.split("d")
                dados.append(dado)

            else:
                bonus.append(int(rolagem))

        valores_por_tdado = []
        valores_rolados = []

        for i in range(len(dados)):
            qntde_dados = int(dados[i][0])
            tipo_dado = int(dados[i][1])

            for _ in range(qntde_dados):
                valores_por_tdado.append(random.randint(1, tipo_dado))
            copia_dos_valores = valores_por_tdado.copy()
            valores_rolados.append(copia_dos_valores)
            valores_por_tdado.clear()

        for i in range(len(valores_rolados)):
            #await ctx.send(str(valores_rolados[i]) + ' :game_die:')
            #await ctx.send(sum(valores_rolados[i]))
            total += sum(valores_rolados[i])
        total += sum(bonus)
        efeito_dano = [":comet:", ":boom:", ":dizzy:"]
        S_N = ["0","1", "2"]
        T_frase = random.choice(S_N)
        verbo = ["Deu", "Mordeu", "Tentou", "Acariciou", "Gemeu", "Pediu", "Colocou", "Fez", "Cobrou",
                 "Chamou", "Regou", "Cavalgou", "Mostrou", "Dedilhou", "Chupou", "Virou", "Tomou", "Sentiu", "Beijou",
                 "Tocou", "Sussurou", "Descobriu", "Cheirou", "Vomitou", "Lambeu", "Assoprou", "Depilou", "Socou",
                 "Imaginou", "Fodeu com força", "Fumou", "Comeu", "Massageou", "Cutucou", "Decorou", "Cortou",
                 "Esfregou", "Bebeu", "Sugou", "Comprou", "Trancou", "Sequestrou", "Escondeu", "Refrescou", "Assistiu",
                 "Ganhou", "Vendeu", "Entortou", "Trancou"
                 ]

        complemento_V = ["os lábios", "um pau", "o mamilo", "a orelha", "o vizinho", "a flauta", "o clitóris", "de 4",
                         "o alazão", "o micropênis", "a goiabeira", "uma surra", "uma mensagem", "o peão", "uma aranha",
                         "seringas", "o joelho", "o dinheiro", "a bunda", "as axilas", "o pulso", "a coxa", "o pescoço",
                         "o bolso", "o relógio", "alguns pentelhos", "a pulseira", "a tiara", "o brinco", "o pau",
                         "a cobra", "o leite", "a descarga", "o ronco", "o ouvidinho virgem", "o bonecão", "o pé",
                         "o baralho", "o anûs", "a língua", "o olho", "o dedo", "o dedo do pé", "a torta", "o pudim",
                         "o pavê", "o pepino", "o toddynho", "o colar", "o umbigo", "a bola", "uma e-girl",
                         "um pack de fotos da foice tortona pra esquerda", "uma maracutaia", "a lâmpada", "o trabalho",
                         "o curso"]

        complemento_V_N = complemento_V.copy()
        nomes = ["o Gabriel", "o João Pedro", "o José", "o Matheus", "o Rafael", "a Thaissa", "o Thiago", "o Victor",
                 "o Lucas", "a Karol"]
        complemento_V_N.extend(nomes)


        complemento_N = ["do Gabriel", "do João Pedro", "do José", "do Matheus", "do Rafael", "da Thaissa",
                         "do Thiago", "do Victor", "do Lucas", "da Karol"]

        Lugares = ["na fila", "no mercado", "no Salesiano", "na árvore", "no bordel", "debaixo da mesa",
                   "em cima da mesa", "na biblioteca do Salesiano", "no ParkShopping", "no Domingão do Faustão",
                   "no armário", "no telhado", "no casório", "no ponto de ônibus", "no Discord", "no bolso",
                   "no RPG", "no chão", "na parede", "na cama", "na cadeira de rodas", "num hospital infantil",
                   "na biblioteca", "na sorveteria", "no sofá", "no córrego", "na lombada", "na gaveta", "no banho",
                   "no vaso", "na janela", "na boca de fumo", "no bueiro", "no Hall da fama", "no Parque", "na lama",
                   "num balanço", "num escorregador", "no trepa-trepa", "no porão do Silvio Santos", "no chiqueiro",
                   "na chuva", "numa lanchonete", "numa bola de demolição"
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
            "karolxp": "Karol"
        }
        cores = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]
        mscleave = discord.Embed(
            title=f'{autistas[autor]}\n{rodada} :game_die:',
            color=random.choice(cores)
        )
        mscleave.add_field(name='E tirou:', value=f'{total} {random.choice(efeito_dano)}')
        await ctx.send(embed=mscleave)
        # embonus = [" :star2:"," :sparkles:", " :zap:"]
        # await message.channel.send(str(sum(bonus)) + random.choice(embonus))
        # await message.channel.send("Você tirou: " + str(total) + random.choice(dano))


    @commands.command()
    async def rolar(self, ctx, *, rolagens):
        total = 0
        quantidade_de_mais = 0
        dados = []
        bonus = []
        rolagens = rolagens.split()
        # mensagem_separada.remove("/roll")

        if "+" in rolagens:
            for i in range(len(rolagens)):
                if rolagens[i] == "+":
                    quantidade_de_mais += 1
            for i in range(quantidade_de_mais):
                rolagens.remove("+")

        for rolagem in rolagens:
            if "d" in rolagem:
                dado = rolagem.split("d")
                dados.append(dado)

            else:
                bonus.append(int(rolagem))

        valores_por_tdado = []
        valores_rolados = []

        for i in range(len(dados)):
            qntde_dados = int(dados[i][0])
            tipo_dado = int(dados[i][1])

            for _ in range(qntde_dados):
                valores_por_tdado.append(random.randint(1, tipo_dado))
            copia_dos_valores = valores_por_tdado.copy()
            valores_rolados.append(copia_dos_valores)
            valores_por_tdado.clear()

        d6b = valores_rolados.copy()
        for i in range(len(valores_rolados)):
            await ctx.send(str(valores_rolados[i]) + ' :game_die:')
            await ctx.send(sum(valores_rolados[i]))
            total += sum(valores_rolados[i])

        d_sucedido = []
        for resultados in d6b:
            for dados_s in resultados:
                dados_s += sum(bonus)
                d_sucedido.append(dados_s)

        sucessos = 0
        for tentativas in d_sucedido:
            if tentativas >= 6:
                sucessos += 1

        total += sum(bonus)
        efeito_dano = [":comet:", ":boom:", ":dizzy:"]
        S_N = ["0", "1", "2"]
        T_frase = random.choice(S_N)
        verbo = ["Deu", "Mordeu", "Tentou", "Acariciou", "Gemeu", "Pediu", "Colocou", "Fez", "Cobrou",
                 "Chamou", "Regou", "Mostrou", "Dedilhou", "Chupou", "Virou", "Tomou", "Sentiu", "Beijou",
                 "Tocou", "Sussurou", "Descobriu", "Cheirou", "Vomitou", "Lambeu", "Assoprou", "Depilou", "Socou",
                 "Imaginou", "Fodeu com força", "Fumou", "Comeu", "Massageou", "Cutucou", "Decorou", "Cortou",
                 "Esfregou", "Bebeu", "Sugou", "Comprou", "Trancou", "Sequestrou", "Escondeu", "Refrescou", "Assistiu",
                 "Ganhou", "Vendeu", "Entortou", "Almoçou"
                 ]

        complemento_V = ["os lábios", "um pau", "o mamilo", "a orelha", "o vizinho", "a flauta", "o clitóris", "de 4",
                         "o alazão", "o micropênis", "a goiabeira", "uma surra", "uma mensagem", "o peão", "uma aranha",
                         "as seringas", "o joelho", "o dinheiro", "a bunda", "as axilas", "o pulso", "a coxa", "o pescoço",
                         "o bolso", "o relógio", "alguns pentelhos", "a pulseira", "a tiara", "o brinco", "o pau",
                         "a cobra", "o leite", "a descarga", "o ronco", "o ouvidinho virgem", "o bonecão", "o pé",
                         "o baralho", "o anûs", "a língua", "o olho", "o dedo", "o dedo do pé", "a torta", "o pudim",
                         "o pavê", "o pepino", "o toddynho", "o colar", "o umbigo", "a bola", "uma e-girl",
                         "um pack de fotos da foice tortona pra esquerda", "uma maracutaia", "a lâmpada", "o trabalho"
                         ]

        complemento_V_N = complemento_V.copy()
        nomes = ["o Gabriel", "o João Pedro", "o José", "o Matheus", "o Rafael", "a Thaissa", "o Thiago", "o Victor",
                 "o Lucas"]
        complemento_V_N.extend(nomes)

        complemento_N = ["do Gabriel", "do João Pedro", "do José", "do Matheus", "do Rafael", "da Thaissa",
                         "do Thiago", "do Victor", "do Lucas"]

        Lugares = ["na fila", "no mercado", "no Salesiano", "na árvore", "no bordel", "debaixo da mesa",
                   "em cima da mesa", "na biblioteca do Salesiano", "no ParkShopping", "no Domingão do Faustão",
                   "no armário", "no telhado", "no casório", "no ponto de ônibus", "no Discord", "no bolso",
                   "no RPG", "no chão", "na parede", "na cama", "na cadeira de rodas", "num hospital infantil",
                   "na biblioteca", "na sorveteria", "no sofá", "no córrego", "na lombada", "na gaveta", "no banho",
                   "no vaso", "na janela", "na boca de fumo", "no bueiro", "no Hall da fama", "no Parque", "num balanço",
                   "num escorregador", "no trepa-trepa", "no porão do Silvio Santos", "no chiqueiro", "na chuva", "na lama",
                   "numa lanchonete", "numa bola de demolição"
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
            "ArtherKobenh": "Gabriel"
        }
        cores = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]
        mscleave = discord.Embed(
            title=f'{autistas[autor]}\n{rodada} :game_die:',
            color=random.choice(cores)
        )
        mscleave.add_field(name='E conseguiu:', value=f'{sucessos} Sucesso(s) {random.choice(efeito_dano)}')
        await ctx.send(embed=mscleave)


def setup(client):
    client.add_cog(Dados(client))
    print("Dados prontos!")