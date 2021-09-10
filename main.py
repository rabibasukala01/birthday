import discord
from discord.ext import commands
import database
import datetime

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())


@client.event
async def on_ready():
    print("ok")


@client.command()
async def addmine(context, month, day, *, name):

    guild_id = context.message.guild.id

    database.add_people(guild_id, name, month, day)
    await context.send("BIRTH DATE ADDED TO DATABASE")


@client.command()
async def todaybirthday(context):
    date_object = datetime.date.today()
    dates = (str(date_object).split("-"))  # yyyy-mm-dd

    guild_id = context.message.guild.id

    data_lists = database.today_bday(int(dates[1]), int(dates[2]), guild_id)
    # data_lists = database.today_bday(9, 7)
    # print(data_lists)

    if len(data_lists) == 0:
        await context.send("NO ONE BORN ON THIS DAY LMAO")
    else:
        for data in data_lists:
            await context.send(data)


client.run(token)
