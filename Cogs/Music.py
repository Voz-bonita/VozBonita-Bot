from __future__ import unicode_literals
import discord
from discord.ext import commands
import youtube_dl
import json
from random import choice
import os
colors = [0x0000FF, 0xFF0000, 0x00FF00, 0x9900FF, 0xFF9900, 0x00FFFF]


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.voice_client = {}
        self.meta = {}

    @commands.command()
    async def join(self, ctx):
        try:
            channel = ctx.author.voice.channel
            self.voice_client = await channel.connect()

        except AttributeError:
            await ctx.send("You gotta be connected to a voice chancel")

        except discord.errors.ClientException:
            await ctx.send("I'm already connected to your voice chanel")

    @commands.command()
    async def leave(self, ctx):
        await self.voice_client.disconnect()
        await ctx.send("Leaving voice channel")
        self.voice_client = {}

    @commands.command()
    async def play(self, ctx, *, song):
        # Stop the current playing song
        self.voice_client.stop()

        # Get all the file names before download the next audio
        downloads = [file for file in os.listdir()]

        # Delete all audios previously downloaded
        # TODO rework it in way that is possible to keep some files arbitrarily
        for file in downloads:
            if file.endswith('.m4a') or file.endswith('.info.json'):
                print(f"Removed {file}")
                os.remove(f"{os.getcwd()}/{file}")
        downloads.clear()

        options = {
            'format': '140',
            'extract audio': True,
            'audio format': 'mp3',
            'outtmpl': f'{song}.%(ext)s',
            'noplaylist': True,
            'writeinfojson': True
        }

        await ctx.send(f":globe_with_meridians: Donwloading")

        with youtube_dl.YoutubeDL(options) as ydl:

            if song.startswith("https://www.youtube.com/"):
                ydl.download([song])

            else:
                ydl.download([f"ytsearch: {song}"])

        song_file = [file for file in os.listdir() if file.endswith('.m4a')][0][:-4]
        
        with open(f'{song_file}.info.json') as file:
            self.meta = json.load(file)
            print(self.meta['fulltitle'])

        self.voice_client.play(discord.FFmpegPCMAudio(f'{song_file}.m4a'))

        # TODO create a way to mark song channel so it doesn't delete normal messages
        await ctx.channel.purge(limit=100)

    @commands.command()
    async def stop(self, ctx):
        self.voice_client.stop()

    @commands.command()
    async def playing(self, ctx):
        # Eventually part of this data can broke and return 0
        date_up = self.meta['upload_date']
        # views = '{:.0f}'.format(self.meta['view_count']/10**3)
        length = self.meta['duration']
        video_info = discord.Embed(
            title=self.meta['fulltitle'],
            color=choice(colors)
        )
        video_info.add_field(name='Title:', value=self.meta['fulltitle'])
        video_info.add_field(name='Channel:', value=self.meta['uploader'])
        video_info.add_field(name='Upload date:', value=date_up[:4] + '/' + date_up[4:6] + '/' + date_up[6:])
        video_info.add_field(name='Length:', value=f'{int(length//60)}min {int(length%60)}s')
        video_info.add_field(name='Likes:', value=self.meta['like_count'])
        video_info.add_field(name='Dislikes:', value=self.meta['dislike_count'])

        await ctx.send(embed=video_info)

    @commands.command()
    async def description(self, ctx):
        # Broke more often than playing command
        
        video_desc = discord.Embed(
            title='Descrição:',
            color=choice(colors)
        )
        video_desc.add_field(name=self.meta['description'], value='')
        await ctx.send(embed=video_desc)

    @commands.command()
    async def resume(self, ctx):
        self.voice_client.resume()

    @commands.command()
    async def pause(self, ctx):
        self.voice_client.pause()

    @commands.command()
    async def volume(self, ctx, volume):
        self.voice_client.source = discord.PCMVolumeTransformer(self.voice_client.source)
        self.voice_client.source.volume = float(volume)


def setup(client):
    client.add_cog(Music(client))
    print("DJ ready!")
