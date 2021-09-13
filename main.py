import discord  # discord==1.7.3#discord.py==1.7.3
from discord.ext import commands
import database
import datetime

client = commands.Bot(command_prefix='?', intents=discord.Intents.all())


@client.event
async def on_ready():
    print("ok")


@client.command()
async def addmine(context, month, day):
    guild_id = str(context.message.guild.id)

    # 1..
    name_of_member = context.author.name
    discriminator_of_member = context.author.discriminator
    id_of_member = context.author.id
    # print(id_of_member)
    # print(type(id_of_member))
    # print("mathi ko")

    # ...
    database.add_people(guild_id, month, day, name_of_member,
                        discriminator_of_member, id_of_member, added=True)
    await context.send("BIRTH DATE ADDED TO DATABASE")


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


@client.command()
async def update(context, month, day):
    guild_id = str(context.message.guild.id)
    id_of_member = context.author.id
    database.update_data(guild_id, id_of_member, month, day)
    await context.send("DATE UPDATED IN DATABASE")


client.run("token")


# daily print(mention) in specific text channel

# 3 dm to specific bithday people
# each member can add only once


# each member can add only once
# --->> make column of "added" 1 for true 0 for false . if date is added to column added make its value to 1. if again user try to add date first see the colum if it is 0 or 1 . if 0 add the date if not print the error statement


# --------------------------------sakyo
# 1 memeber ko naam liney automatic and mention them
# 2 update date if wrong{# update date if wrong
# --->> DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';OR
# UPDATE employees
# SET
#     column1=value,column2=value, ......
# WHERE
#     condition;


# naya kura thapako
# await context.author.send("aa")
