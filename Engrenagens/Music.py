from __future__ import unicode_literals
import discord
from discord.ext import commands
import youtube_dl
import json
import random

class Musica(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def join(self, ctx):
        try:
            canal = ctx.author.voice.channel
            global voice_client
            voice_client = await canal.connect()

        except AttributeError:
            await ctx.send("You gotta be connected to a voice chancel")

        except discord.errors.ClientException:
            await ctx.send("I'm already connected to your voice chanel")

    @commands.command()
    async def leave(self, ctx):
        try:
            await voice_client.disconnect()
            await ctx.send("Leaving voice channel")

        except NameError:
            await ctx.send("I'm not connected to any voice channel :worried:")

    @commands.command()
    async def play(self, ctx, *, musica):
        try:
            if ctx.author != "JP33#8256":

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

                with open(f'{musica}.info.json') as file:
                    global meta
                    meta = json.load(file)
                    print(meta['fulltitle'])

                voice_client.play(discord.FFmpegPCMAudio(f'{musica}.m4a'))



        except NameError:
            await ctx.send("I'm not connected to any voice channel :worried:")

        except:
            with open(f'{musica}.info.json') as file:
                global meta2
                meta2 = json.load(file)
                print(meta['fulltitle'])

            voice_client.play(discord.FFmpegPCMAudio(f'{musica}.m4a'))




    @commands.command()
    async def stop(self, ctx):
        voice_client.stop()

    @commands.command()
    async def playing(self, ctx):
        cores = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]
        autor = str(ctx.author)
        date_up = meta['upload_date']
        views = '{:.0f}'.format(meta['view_count']/10**3)
        duracao = meta['duration']
        video_info = discord.Embed(
            title=meta['fulltitle'],
            color=random.choice(cores)
        )
        video_info.add_field(name='Title:',value=meta['fulltitle'])
        video_info.add_field(name='Channel:', value=meta['uploader'])
        video_info.add_field(name='Upload date:', value=date_up[:4] + '/' + date_up[4:6] + '/' + date_up[6:])
        video_info.add_field(name='Length:', value=f'{int(duracao//60)}min {int(duracao%60)}s')
        video_info.add_field(name='Dislikes:', value=meta['dislike_count'])
        video_info.add_field(name='Likes:', value=meta['like_count'])

        await ctx.send(embed=video_info)

    @commands.command()
    async def description(self, ctx):
        cores = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]
        video_desc = discord.Embed(
            title='Descrição:',
            color=random.choice(cores)
        )
        video_desc.add_field(name=meta['description'], value='')
        await ctx.send(embed=video_desc)

    @commands.command()
    async def resume(self, ctx):
        voice_client.resume()

    @commands.command()
    async def pause(self, ctx):
        voice_client.pause()

    @commands.command()
    async def volume(self, ctx, volume):
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
        voice_client.source.volume = float(volume)



def setup(client):
    client.add_cog(Musica(client))
    print("Música pronta!")