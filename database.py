import sqlite3


def connect_to_db(guild_id):

    return sqlite3.connect(f'{guild_id}.db')
   # cursor = connection.cursor()

   # return cursor


def create(guild_id, connection):

    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS PEOPLE (SN INTEGER PRIMARY KEY,ID INTEGER ,NAME STRING ,DISCRIMINATOR STRING ,MONTH INTEGER ,DAY INTEGER );")


def add_people(guild_id, month, day, name, discriminator, id_of_member):
    connection = connect_to_db(guild_id)
    create(guild_id, connection)
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
    create(guild_id, connection)
    newIDlists = []

    with connection:

        IDlists = connection.execute(
            "SELECT ID FROM PEOPLE WHERE MONTH=? AND DAY =?;", (today_month, today_day))

        for lists in IDlists:
            newIDlists.append(lists)  # each element in list is tuple
        # print(newIDlists)
        return newIDlists


def update_data(guild_id, memberID, month, day):
    connection = connect_to_db(guild_id)
    create(guild_id, connection)
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
