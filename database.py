import sqlite3


def connect_to_db(guild_id):
    connection = sqlite3.connect(f'{guild_id}.db')
    cursor = connection.cursor()
    return cursor


def create(guild_id):
    cursor = connect_to_db(guild_id)

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS PEOPLE (id INTEGER PRIMARY KEY,NAME STRING ,MONTH INTEGER ,DAY INTEGER )")


def add_people(guild_id, name, month, day):
    cursor = connect_to_db(guild_id)
    create(guild_id)
    cursor.execute(
        "INSERT INTO PEOPLE (NAME,MONTH ,DAY)VALUES(?,?,?);", (name, month, day))
    # cause connection halyo vaney ta not define vai halxa ni
    connection = sqlite3.connect(f'{guild_id}.db')
    connection.commit()


def today_bday(today_month, today_day, guild_id):
    cursor = connect_to_db(guild_id)
    create(guild_id)
    newList = []

    NAMES = cursor.execute(
        "SELECT NAME FROM PEOPLE WHERE MONTH=? AND DAY =?;", (today_month, today_day))

    for name in NAMES:
        newList.append(name[0])
        print(name)
    return newList


# def debugshow():
#     return cursor.execute("SELECT * FROM PEOPLE").fetchall()
