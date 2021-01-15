import discord
import random
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from discord.ext import commands
import time
import youtube_dl
import datetime
#driver = webdriver.Chrome("C:\\Users\\jose_\\Desktop\\CDriver\\chromedriver")
client = discord.Client()
players ={}
teste = {}
cores = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]
bot = commands.Bot(command_prefix='/')
class bcolors:
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"

@client.event
async def on_ready():
    print('Tô ligado, pai')

@client.event
async def on_message(message):
    mensagem = message.content.capitalize()
    if mensagem.startswith("!a"):
        timestamp = time.time()
        if message.author not in teste:
            teste[message.author] = timestamp
            print("aaaaa")
        elif timestamp >= teste[message.author] + 10:
            teste[message.author] = timestamp
            print("bbbb")

        else:
            print("on cd")

    if mensagem.startswith("/entrar"):
        canal = message.author.voice.channel
        global voice_client
        voice_client = await canal.connect()

    if mensagem.startswith("/entrar"):
        musica = mensagem[8:]

        voice_client.stop()
        options = {
            'format': '140',
            'extract audio': True,
            'audio format': 'mp3',
            'outtmpl': f'{musica}.%(ext)s',
            'noplaylist': True,
            'writeinfojson': True
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            if musica.startswith("https://www.youtube.com/"):
                ydl.download([musica])

            else:
                ydl.download([f"ytsearch: {musica}"])

            voice_client.play(discord.FFmpegPCMAudio(f'{musica}.m4a'))

    if message.content.lower().startswith('hamdii'):
        await message.channel.send(message)

    if mensagem.startswith("?help"):
        await message.channel.send("• /Entrar (Entra no canal de voz)" + "\n" +
                                   "• /Play (Toca música)" + "\n" +
                                   "• /Playing (Mostra o que ta tocando)" + "\n" +
                                   "• /Pause (Pausa a música)" + "\n" +
                                   "• /Unpause (Despausa a música)" + "\n" +
                                   "• /Stop (Para a música)")

    if mensagem.startswith("/entrar"):
        try:
            channel = message.author.voice.channel
            vc = await channel.connect()

        except AttributeError:
            await message.channel.send("Você precisa estar conectado a um canal de voz")

        except discord.errors.ClientException:
            await message.channel.send("Eu já estou conectado ao seu canal de voz")

    if mensagem.startswith("/sair"):
        await discord.VoiceClient.disconnect(discord.VoiceClient, force = False)


    if mensagem.startswith("/play"):
        url = message.content[6:]
        voice = client.voice.channel(messsage.guild)
        print(voice)
        players[message.server.id].stop()
        player = await voice.create_ytdl_player('ytsearch: {}'.format(url))
        players[message.server.id] = player
        player.start()


    if mensagem.startswith("?rpg"):
        await message.channel.send("• /Roll [Quantidade de dados]d[Quantidade de faces do dado] + [Bônus, se necessário]")

    if mensagem.startswith("/roll") and len(mensagem) <= 27:
        #if message.author == discord.member.Member(José#0237):
            #await message.channel.send("Você é um merda, eu não tenho que rolar dados pra você")
        total = 0
        quantidade_de_mais = 0
        dados = []
        bonus = []
        mensagem_separada = mensagem.split()
        mensagem_separada.remove("/roll")

        if "+" in mensagem_separada:
            for i in range(len(mensagem_separada)):
                if mensagem_separada[i] == "+":
                    quantidade_de_mais += 1
            for i in range(quantidade_de_mais):
                mensagem_separada.remove("+")

        for rolagem in mensagem_separada:
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
            #await message.channel.send(str(valores_rolados[i]) + ' :game_die:')
            #await message.channel.send(sum(valores_rolados[i]))
            total += sum(valores_rolados[i])
        total += sum(bonus)
        efeito_dano = [":comet:", ":boom:", ":dizzy:"]

        roda = ["Deu descarga", "Foi dormir", "Entrou no urso ( ͡° ͜ʖ ͡°)", "Agora se chama Wanderley",
                "Mordeu os lábios", "Motrou todos os seus 3 mamilos", "Testou soro positivo", "Comeu o cú de quem ta lendo",
                "Está roncando", "Colocou uma camisinha", "Mostrou o pau", "Mostrou o mamilo",
                "Mordeu o bumbumzinho do Victor", "Escovou o clarinete do Victor", "Trocou as cordas do Victor",
                "Acariciou o arcebispo do Thiago", "Penteou o avestruz do Thiago", "Ralou coxa com o Thiago",
                "Está mandando mensagem pra mãe do Thiago",
                "Cavalgou no Alazão do Matheus", "Compartilhou seringas com o Matheus", "Beijou o irmão do Matheus",
                "Está imaginando o Matheus nú",
                "Socou o pau do João Pedro", "Pediu o João Pedro em casamento", "Dedilhou o micropênis do João Pedro",
                "Afinou o João Pedro",
                "Roubou a namorada do José", "Caiu nos encantos do José", "Cobrou dinheiro do José",
                "Assoprou a flauta do Gabriel", "Mordeu a flauta do Gabriel", "Penteou o elefante do Gabriel",
                "Esmerilhou o cano do Gabriel",
                "Deu uma cabeçada no joelho da Thaissa", "Deixou a Thaissa de joelhos", "Regou a goiabeira da Thaissa",
                "Chamou o vizinho da Thaissa",
                "Virou um copo de whisky", "Furou o RPG", "Ficou de 4", "Está com uma prostituta no colo",
                "Saiu do armário", "Tomou uma surra de anão", "Gemeu alto", "Gemeu baixinho",
                "Sentiu algo pegando na sua bunda", "Leu um livro", "Fez um bot", "Se depilou", "Chupou um pirulito",
                "Ganhou um par de chifres"]
        autor = str(message.author)
        autor = autor[:-5]
        autistas = {
            "cobrador73" : "Matheus",
            "Schezo, The Dark Mage" : "Gabriel",
            "JP33" : "João Pedro",
            "Rafalula" : "Rafael",
            "DryiaKitsune" : "Thaissa",
            "Ishida Maki" : "Thiago",
            "Gordon2" : "Victor",
            "Snorcs" : "José"
        }
        mscleave = discord.Embed(
            title = f'{autistas[autor]}\n{random.choice(roda)} :game_die:',
            color = random.choice(cores)
        )
        mscleave.add_field(name = 'E tirou:', value = f'{total} {random.choice(efeito_dano)}')
        await message.channel.send(embed = mscleave)
        #embonus = [" :star2:"," :sparkles:", " :zap:"]
        #await message.channel.send(str(sum(bonus)) + random.choice(embonus))
        #await message.channel.send("Você tirou: " + str(total) + random.choice(dano))



