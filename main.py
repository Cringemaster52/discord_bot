import discord
from discord.ext import commands

import random
import os
import requests

list_eco = ['Найдите ближайший к вам контейнер, куда сможете относить мусор для переработки.', 'Обращайте внимание на вид упаковки еще в магазине.',
'Помните, что отсортированный мусор должен быть чистым.',
'Постарайтесь готовить еду самостоятельно, чтобы брать на работу в своем контейнере.',]

list_facts = ['Ежегодно на Земле высаживается лишь около 10% деревьев от того их числа, которое вырубается за тот же срок.', 
              'В Тихом океане есть мусорное пятно, площадь которого достигает 1,5 млн км²', 
              'Для производства экологически чистых электромобилей используется масса вредных технологий, загрязняющих окружающую среду.', 
              'Выбросы парниковых газов, останутся в атмосфере в течение многих лет, делая невозможным устранение проблемы глобального потепления на протяжении нескольких десятилетий.']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Я бот {bot.user}!' 
                   '\n$mem - присылает мем'
                   '\n$facts - присылает факты'
                   '\n$eco - советы про экологию')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def facts(ctx):
    fact = random.choice(list_facts)
    await ctx.send(fact)

@bot.command()
async def eco(ctx):
    sovet = random.choice(list_eco) 
    await ctx.send(sovet)

bot.run("TOKEN")
