import requests
import discord
import random
from discord.ext import commands
import os
#print(os.listdir('images'))

bot = commands.Bot(command_prefix="$", intents=discord.Intents.default())
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print("Loaded")

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run("MTE1OTg4MDE0Njg2MjQ5MzcxNg.GMLmlk.jkYBbxb2Sw9yOXKrwKgJ-cyW54bUSKBTT5_ME0")