import discord
import os
from dotenv import load_dotenv
from typing import Final    

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$henrique quitou"):
        await message.channel.send("Henrique é um grande merda!")

load_dotenv()
TOKEN: Final[str] = os.getenv("TOKEN")

if TOKEN is None:
    print("A variável de ambiente TOKEN não está definida corretamente.")
else:
    client.run(TOKEN)