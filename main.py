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
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times:int, content='repeating...'):
    """reapeats a message a multiple times"""
    for i in range(times):
        await ctx.send(content)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command('fox')
async def fox(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

list = ['Найдите ближайший к вам контейнер, куда сможете относить мусор для переработки.', 'Обращайте внимание на вид упаковки еще в магазине.',
'Помните, что отсортированный мусор должен быть чистым.',
'Постарайтесь готовить еду самостоятельно, чтобы брать на работу в своем контейнере.',]

@bot.command()
async def eco(ctx):
    sovet = random.choice(list) 
    await ctx.send(sovet)

bot.run("TOKEN")
