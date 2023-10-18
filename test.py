import discord
import requests
import json
import os
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Salut mon pote cest {self.user}!')

    async def on_message(self, message):
        if (message.author != self.user):
            await message.channel.send('salut', file=discord.File('./convert/meme_scale.jpg'))

intents = discord.Intents.default()
intents.message_content = True

with open('config.json') as f:
    data = json.load(f)
    token = data["token"]

client = MyClient(intents=intents)
client.run(token)
