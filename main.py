import discord  # discord==1.7.3#discord.py==1.7.3
from discord.ext import commands
import database
import datetime
import time
import os
from dotenv import load_dotenv
load_dotenv('.env')
token = os.getenv('TOKEN')

client = commands.Bot(command_prefix='?',
                      intents=discord.Intents.all(), help_command=None)


@client.event
async def on_ready():
    print("ok")


@client.command()
async def help(context):
    await context.send("help command styling gardeu na ")


@client.command()
async def addmine(context, month, day):
    guild_id = str(context.message.guild.id)

    # 1..
    name_of_member = context.author.name
    discriminator_of_member = context.author.discriminator
    id_of_member = (context.author.id)
    # print(id_of_member)
    # print(type(id_of_member))

    # ...

    text = database.add_people(guild_id, month, day, name_of_member,
                               discriminator_of_member, id_of_member)
    await context.send(text)


@ client.command()
async def todaybirthday(context):
    date_object = datetime.date.today()

    dates = str(date_object).split("-")  # yyyy-mm-dd
    guild_id = str(context.message.guild.id)
    data_lists = database.today_bday(int(dates[1]), int(dates[2]), guild_id)
# data_list ma  lists   ko element is in tuple
    if len(data_lists) == 0:
        await context.send("NO ONE BORN ON THIS DAY LMAO")

    else:
        for data in data_lists:
            # print(data)

            await context.send(f'<@!{data[0]}>, Birthday ko suvakamana xa !')
            user = dm(data[0])
            await user.send("Birthday ko suvakamana xa")


def dm(userid):
    return (client.get_user(userid))


@client.command()
async def update(context, month, day):
    guild_id = str(context.message.guild.id)
    id_of_member = context.author.id
    database.update_data(guild_id, id_of_member, month, day)
    await context.send("DATE UPDATED IN DATABASE")


# @client.command()
# async def ping(context):
#     await context.send(f"{round(client.latency*1000)}ms")


client.run(token)


# daily print(mention) in specific text channel


# --------------------------------sakyo---------------
# 1 memeber ko naam liney automatic and mention them


# 2 update date if wrong{# update date if wrong
# --->> DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';OR
# UPDATE employees
# SET
#     column1=value,column2=value, ......
# WHERE
#     condition;

# 3 each member can add only once- search in database for specific id. then if it is exist ignore else add to database

# 4 dm to specific bithday people


# naya kura thapako
# await context.author.send("aa")
