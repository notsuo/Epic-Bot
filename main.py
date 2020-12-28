import settings
import discord
from discord.ext import tasks
from datetime import datetime

TOKEN = settings.token
CHANNEL_ID = 791282157523959850

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('______')

@client.event
async def on_message(message):
    if message.content.startswith("おはよう"):
        if client.user != message.author:
            m = "おはようございます" + message.author.name + "さん！"

            await message.channel.send(m)

    if message.content.startswith('!start'):
        if client.user != message.author:
            loop.start()
            await message.channel.send('Epic Bot Start')

    if message.content.startswith('!stop'):
        if client.user != message.author:
            loop.stop()
            await message.channel.send('Epic Bot Stop')



@tasks.loop(seconds=60)
async def loop():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    now = datetime.now().strftime('%H:%M')
    if now == '07:00' or now == '19:00':
        await channel.send('Epic Games')

client.run(TOKEN)