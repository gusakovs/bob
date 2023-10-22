import random
import discord
import requests
import json
import os
import time
from wand.image import Image
from random_word import RandomWords

def dl_image(atach):
    img_data = requests.get(atach.url).content
    r = RandomWords()

    word = r.get_random_word()
    with open('./convert/' + word + '.jpg', "wb") as handler:
        handler.write(img_data)

    return word

async def seam(message):
    name = dl_image(message.attachments[0])
    
    image = Image(filename='./convert/' + name + '.jpg')

    with image.clone() as liquid:
        liquid.liquid_rescale(int(image.width*0.95), int(image.height*0.75))
        liquid.save(filename='./convert/' + name + '_crop.jpg')

    await message.channel.send(file=discord.File('./convert/' + name + '_crop.jpg'))

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

'''
with open('ids.json') as f:
    data = json.load(f)
    maxime = data["maxime"]
    memeid = data["memeid"]
'''
client = MyClient(intents=intents)
client.run(token)
