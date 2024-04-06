import discord
from discord.ext import commands

import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!' 
                   '\n$mem - присылает мем'
                   '\n$facts - присылает факты'
                   '\n$eco - советы про экологию')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


list = ['Найдите ближайший к вам контейнер, куда сможете относить мусор для переработки.', 'Обращайте внимание на вид упаковки еще в магазине.',
'Помните, что отсортированный мусор должен быть чистым.',
'Постарайтесь готовить еду самостоятельно, чтобы брать на работу в своем контейнере.',]

@bot.command()
async def eco(ctx):
    sovet = random.choice(list) 
    await ctx.send(sovet)

bot.run("TOKEN")
