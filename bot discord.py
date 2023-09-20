import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


commands_list = ["hello", "heh", "secretURL", "kawaii", "helps"]


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
async def secretURL(ctx):
    embed = discord.Embed(
        title="Тык для перехода",
        description="Ссылка для перехода на кота",
        url='https://imgur.com/gallery/eslTP',
    )
    await ctx.send(embed=embed)


@bot.command()
async def kawaii(ctx):
    await ctx.send(f'Пользователь, я считаю вы очень милы :з')


@bot.command()
async def helps(ctx):
    await ctx.send(commands_list)

bot.run("MTE0OTAwODMwMjM4MzA1OTExNg.G3PZuR.eBL82JYmVqMov4ECJKSILTKYIjYCVbl7T9m56o")