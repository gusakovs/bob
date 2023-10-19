import random
import discord
import requests
import json
import os
import time

async def seam(message):
    attachment = message.attachments[0]

    w = random.randint(30, 115)
    c = w + (w * 0.25)
    
    img_data = requests.get(attachment.url).content
    with open("./convert/meme.jpg", "wb") as handler:
        handler.write(img_data)

        os.system('magick ./convert/meme.jpg -liquid-rescale 70x70%\! ./convert/meme_scale.jpg')
    await message.channel.send(file=discord.File('./convert/meme_scale.jpg'))



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Salut mon pote cest {self.user}!')

    async def on_message(self, message):
        if (message.author == self.user):
            return
        if(message.attachments):
            await seam(message)



intents = discord.Intents.default()
intents.message_content = True

with open('config.json') as f:
    data = json.load(f)
    token = data["token"]

with open('ids.json') as f:
    data = json.load(f)
    maxime = data["maxime"]
    memeid = data["memeid"]

client = MyClient(intents=intents)
client.run(token)
