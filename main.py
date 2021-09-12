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


client.run("ODg1NTE3MjQ2NzM3MjkzMzQy.YToMMw.I1zFNx2Wok8h_IcAN8yzm-EcyVU")
