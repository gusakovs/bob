import random
import discord
import requests
import json
import os
import time
from wand.image import Image
from random_word import RandomWords
from discord import app_commands


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
    
    i = 1

    with image.clone() as liquid:
        liquid.liquid_rescale(int(image.width*0.65), int(image.height*0.45))
        if i:
            liquid.modulate(100,200,100)
            liquid.brightness_contrast(0.0, 60)
            liquid.adaptive_sharpen(10.2, 4.3)
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

client = MyClient(intents=intents)
client.run(token)
tree = app_commands.CommandTree(client)

@tree.command(name="coucou-mv")
async def foo(ctx, arg):
    ctx.send(arg)
