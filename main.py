import pytz
import datetime

import asyncio
import discord  # discord==1.7.3#discord.py==1.7.3
from discord.ext import commands
import database

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

            # await context.send(f'<@!{data[0]}>, Birthday ko suvakamana xa !')
            await context.send(f'<@!{data[0]}>, Birthday ko suvakamana xa !')


def dm(userid):
    return (client.get_user(userid))


@client.command()
async def updatedate(context, month, day):
    guild_id = str(context.message.guild.id)
    id_of_member = context.author.id
    database.update_date(guild_id, id_of_member, month, day)
    await context.send("DATE UPDATED IN DATABASE")


@client.command()
async def ping(context):
    await context.send(f"{round(client.latency*1000)}ms")


@client.command()
async def addchannel(context, channelname):
    # await context.send(channelname)
    channelname = channelname.replace("<", "")
    channelname = channelname.replace(">", "")
    channelname = channelname.replace("#", "")
    guild_id = str(context.message.guild.id)
    text = database.add_channel(guild_id, channelname)
    # channel = database.access_to_guild_channel(guild_id)
    # print(type(channel))
    print(text)


@client.command()
async def updatechannel(context, channelname):
    guild_id = str(context.message.guild.id)
    channelname = channelname.replace("<", "")
    channelname = channelname.replace(">", "")
    channelname = channelname.replace("#", "")
    text = database.update_channel(guild_id, channelname)
    await context.send(text)


# async def background():
#     await client.wait_until_ready()
#     tz_ktm = pytz.timezone('Asia/Kathmandu')
#     datetime_Kathmandu = datetime.datetime.now(tz_ktm)

#     timevariable = (datetime_Kathmandu.strftime("%H:%M:%S"))
#     timelist = timevariable.split(":")
#     date_object = datetime.date.today()  # yyyy-mm-dd
#     dates = str(date_object).split("-")
#     month = int(dates[1])
#     day = int(dates[2])
#     hour = int(timelist[0])
#     minute = int(timelist[1])
#     second = int(timelist[2])

#     while not client.is_closed():
#         if (hour == 16 and minute == 15 and second == 0):  # H:M:S

#             channels = database.access_to_guild_channel()

#             counter = 0
#             guild_id = database.guild_extractor()

#         for c in channels:
#             channel = client.get_channel(c[0])

#             if len(data_lists) == 0:
#                 await channel.send("NO ONE BORN ON THIS DAY LMAO")

#             counter += 1
#             await channel.send(counter)

# # async def background():
#     # await client.wait_until_ready()
#     # channel = client.get_channel(885502487346417695)
#     # counter = 0
#     # while not client.is_closed():

#     #     counter += 1
#     #     await channel.send(counter)


# async def background():
#     await client.wait_until_ready()

#     while True:
#         # -------------------
#         # times and date
#         tz_ktm = pytz.timezone('Asia/Kathmandu')
#         datetime_Kathmandu = datetime.datetime.now(tz_ktm)

#         timevariable = (datetime_Kathmandu.strftime("%H:%M:%S"))
#         timelist = timevariable.split(":")
#         date_object = datetime.date.today()  # yyyy-mm-dd
#         dates = str(date_object).split("-")
#         month = int(dates[1])
#         day = int(dates[2])
#         hour = int(timelist[0])
#         minute = int(timelist[1])
#         second = int(timelist[2])
#         # --------------------
#         if (hour == 19 and minute == 43 and second == 0):
#             guild_id_list = database.guild_extractor()
#             for guild_id in guild_id_list:
#                 channel = client.get_channel(database.showchannelid(guild_id))

#                 await channel.send("1840")

#         await asyncio.sleep(10)


async def background():
    await client.wait_until_ready()

    while True:
        tz_ktm = pytz.timezone('Asia/Kathmandu')
        datetime_Kathmandu = datetime.datetime.now(tz_ktm)

        timevariable = (datetime_Kathmandu.strftime("%H:%M:%S"))
        timelist = timevariable.split(":")
        date_object = datetime.date.today()  # yyyy-mm-dd
        dates = str(date_object).split("-")
        month = int(dates[1])
        day = int(dates[2])
        hour = int(timelist[0])
        minute = int(timelist[1])
        second = int(timelist[2])

        # --------------------
        if (hour == 0 and minute == 0 and second == 0):

            # print(second)
            guild_id_list = database.guild_extractor()
            for guild_id in guild_id_list:
                channel = client.get_channel(database.showchannelid(guild_id))
                data_lists = database.today_bday(
                    int(dates[1]), int(dates[2]), guild_id)

                # await channel.send("1840")
                if len(data_lists) == 0:
                    await channel.send("NO ONE BORN ON THIS DAY LMAO")

                else:
                    for data in data_lists:
                        # print(data)

                        await channel.send(f'<@!{data[0]}>, Birthday ko suvakamana xa !')
                        user = dm(data[0])
                        await user.send("Birthday ko suvakamana xa")

        await asyncio.sleep(1)

client.loop.create_task(background())
client.run(token)


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
# 5 daily print(mention) in specific text channel

# naya kura thapako
# await context.author.send("aa")
