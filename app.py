import os
from typing import Final
import discord
from discord.ext import commands
from dotenv import load_dotenv
import youtube_dl

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

quit_count = 0  # Variável global para contar o número de vezes que a mensagem foi enviada

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    global quit_count

    if message.author == client.user:
        return

    await client.process_commands(message)  # Adicione esta linha para processar comandos após verificar mensagens

    content_lower = message.content.lower()

    if content_lower.startswith("!henrique quitou"):
        quit_count += 1
        await message.channel.send(f"O Henrique quitou {quit_count} vezes, e é um vacilão!")

    elif content_lower.startswith("!perillo vai estudar"):
        await message.channel.send("Perillo, largue de ser um merda e vai estudar!")

    elif content_lower.startswith("!vasco"):
        await message.channel.send("Coitado do Vasco, não ganha nada, só uma passagem vip pra série B!")

load_dotenv()
TOKEN: Final[str] = os.getenv("TOKEN")

if TOKEN is None:
    print("A variável de ambiente TOKEN não está definida corretamente.")
else:
    client.run(TOKEN)
