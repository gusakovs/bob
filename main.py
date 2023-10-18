import discord
import requests

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Salut mon pote cest {self.user}!')

    async def on_message(self, message):
        attachment = message.attachments[0]

        img_data = requests.get(attachment.url).content
        with open("./meme.jpg", "wb") as handler:
            handler.write(img_data)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTE1ODA2ODA2MTA0MDAzNzkzOQ.GNBldT.mhb6ifOolWIjZLWobztoWEaPoPVYvr1BxqGHZ0')
