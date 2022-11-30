import discord
import bot_func
import datetime
from time import asctime
from discord.ext import commands
from config import settings


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


@bot.command()
async def week(ctx):
    await ctx.send(f"Сегодня {bot_func.which_week()} неделя")


@bot.command()
async def today_schedule(ctx):
    wk = bot_func.which_week()
    await ctx.send(bot_func.schedule(wk, asctime().split()[0]))


@bot.command()
async def tmrw_schedule(ctx):
    wk = bot_func.which_week()
    tmrw = datetime.date.today() + datetime.timedelta(days=1)

    await ctx.send(bot_func.schedule(wk, tmrw.strftime('%A')[:3]))


@bot.command()
async def full_schedule(ctx):
    wk = bot_func.which_week()
    await ctx.send(bot_func.schedule(wk, 'every'))


bot.run(settings['token'])