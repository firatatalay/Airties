import sqlite3
from datetime import datetime

con = sqlite3.connect("db.sqlite", check_same_thread=False)
cursor = con.cursor()


def getData():
    '''All data is fetched from the persons table and displayed in descending order of creation date.'''
    return cursor.execute("SELECT * FROM persons ORDER BY created_date DESC;").fetchall()


def createTable():
    cursor.execute('''CREATE TABLE persons (
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        first_name TEXT, 
        last_name TEXT,
        email TEXT,
        phone TEXT, 
        created_date timestamp)''')
    con.commit()


def addData(first_name, last_name, email, phone):
    cursor.execute('''
        INSERT INTO PERSONS ('first_name', 'last_name', 'email', 'phone', 'created_date') VALUES(?,?,?,?,?)''', 
        (first_name, last_name, email, phone, datetime.now()))
    con.commit()


persons = [('Fırat', 'Atalay', 'firat@firat.com', '+11111'),
           ('Airties', 'Kullanici1', 'Airties1@airties.com', '+22222'),
           ('Airties', 'Kullanici2', 'Airties2@airties.com', '+33333')
           ]

#createTable()

#for person in persons:     #The data in the Person list is sent sequentially to the addData function and saved in the database.
#    addData(*person)

#con.close()
