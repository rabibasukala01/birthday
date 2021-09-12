import sqlite3


def connect_to_db(guild_id):

    return sqlite3.connect(f'{guild_id}.db')
   # cursor = connection.cursor()

   # return cursor


def create(guild_id, connection):

    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS PEOPLE (SN INTEGER PRIMARY KEY,ID INTEGER ,NAME STRING ,DISCRIMINATOR STRING ,MONTH INTEGER ,DAY INTEGER ,ADDED BOOL)")


def add_people(guild_id, month, day, name, discriminator, id_of_member, added):
    connection = connect_to_db(guild_id)

    with connection:
        create(guild_id, connection)
        connection.execute(
            "INSERT INTO PEOPLE (ID ,NAME,DISCRIMINATOR,MONTH ,DAY,ADDED)VALUES(?,?,?,?,?,?);", (id_of_member, name, discriminator, month, day, added))

    connection.commit()


def today_bday(today_month, today_day, guild_id):
    connection = connect_to_db(guild_id)
    create(guild_id, connection)
    newIDlists = []

    with connection:

        IDlists = connection.execute(
            "SELECT ID,ADDED FROM PEOPLE WHERE MONTH=? AND DAY =?;", (today_month, today_day))

        for lists in IDlists:
            newIDlists.append(lists)  # each element in list is tuple
        print(newIDlists)
        return newIDlists


# def debugshow():
#     return cursor.execute("SELECT * FROM PEOPLE").fetchall()
# today_bday(9, 12, 885502487346417695)
# add_people(885502487346417695, 9, 12, 'rara',
#            9898, 717730586843938846, added=True)
# today_bday(9, 12, 885502487346417695)
