
import sqlite3
import os


def connect_to_db(guild_id):

    return sqlite3.connect(f'{guild_id}.db')
   # cursor = connection.cursor()

   # return cursor


def create(connection):

    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS PEOPLE (SN INTEGER PRIMARY KEY,ID INTEGER ,NAME STRING ,DISCRIMINATOR STRING ,MONTH INTEGER ,DAY INTEGER );")


# ---------------------------


def create_db_for_channel_id(connection):
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS CHANNEL(SN INTEGER PRIMARY KEY,GUILD_ID INTEGER,CHANNELID INTEGER);")


def add_channel(guild_id, channel_id):
    connection = connect_to_db(guild_id)
    create_db_for_channel_id(connection)
    with connection:
        TEST_IF_GUILD_ID_AVAILABLE = connection.execute(
            'SELECT GUILD_ID FROM CHANNEL WHERE GUILD_ID=?;', (guild_id,))
        if TEST_IF_GUILD_ID_AVAILABLE.fetchall() != []:
            return "already in database"
        else:
            connection.execute(
                "INSERT INTO CHANNEL(GUILD_ID,CHANNELID)VALUES(?,?);", (guild_id, channel_id))
            return "channel added"
    connection.commit()

# //guild nikalya files name bata nai


def guild_extractor():
    guild_id_list = []
    files = os.listdir()
    for f in files:
        if f.endswith(".db"):
            var = f.split(".")
            guild_id_list.append(var[0])
    return guild_id_list


def showchannelid(guild_id):

    connection = connect_to_db(guild_id)
    create_db_for_channel_id(connection)
    with connection:
        va = connection.execute("SELECT CHANNELID FROM CHANNEL; ")

        return(va.fetchall()[0][0])


def update_channel(guild_id, channelname):

    connection = connect_to_db(guild_id)
    create_db_for_channel_id(connection)
    with connection:
        connection.execute(
            "UPDATE CHANNEL SET CHANNELID = ?  WHERE GUILD_ID = ?;", (channelname, guild_id))
    return "success"
# ---------------------------


def add_people(guild_id, month, day, name, discriminator, id_of_member):
    connection = connect_to_db(guild_id)
    create(connection)
    with connection:

        TEST_IF_ID_AVAILABLE = connection.execute(
            "SELECT ID FROM PEOPLE WHERE ID=?;", (id_of_member,))

        if TEST_IF_ID_AVAILABLE.fetchall() != []:
            return "ALREADY IN DATABASE TRY UPDATING DATE IF ENTERED INCORRECTLY"
        else:
            connection.execute(
                "INSERT INTO PEOPLE (ID ,NAME,DISCRIMINATOR,MONTH ,DAY)VALUES(?,?,?,?,?);", (id_of_member, name, discriminator, month, day))
            return "ADDED TO DATABASE"

    connection.commit()


def today_bday(today_month, today_day, guild_id):
    connection = connect_to_db(guild_id)
    create(connection)
    newIDlists = []

    with connection:

        IDlists = connection.execute(
            "SELECT ID FROM PEOPLE WHERE MONTH=? AND DAY =?;", (today_month, today_day))

        for lists in IDlists:
            newIDlists.append(lists)  # each element in list is tuple
        # print(newIDlists)
        return newIDlists


def update_date(guild_id, memberID, month, day):
    connection = connect_to_db(guild_id)
    create(connection)
    with connection:
        connection.execute(
            "UPDATE PEOPLE SET MONTH = ? , DAY= ? WHERE ID = ?;", (month, day, memberID))


# def debugshow():
#     return cursor.execute("SELECT * FROM PEOPLE").fetchall()
# today_bday(9, 12, 885502487346417695)
# add_people(885502487346417695, 9, 12, 'rara',
#            9898, 717730586843938846, added=True)
# update_data(885502487346417695, 717730586843938846, 9, 13)


# today_bday(9, 13, 885502487346417695)
# connection = connect_to_db(871619898852393070)
# with connection:
#     create(871619898852393070, connection)
#     TEST_IF_ID_AVAILABLE = connection.execute(
#         "SELECT ID FROM PEOPLE WHERE ID=?;", (717730586843938846,))

# print(TEST_IF_ID_AVAILABLE.fetchall())
# if TEST_IF_ID_AVAILABLE.fetchall() == []:
#     print("lol")


# channel = access_to_guild_channel()
# print(type(channel))
# for c in channel:
#     print(c[0])


# gg = guild_extractor()
# print(gg)
