import sqlite3
import requests
import sys
import json



conn=sqlite3.connect("shopping_list.db")
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS shopping_list( title TEXT, description TEXT)")
def data_entry():
    c.execute("INSERT INTO shopping_list VALUES('milk', 'to put on my coffee')")
    conn.commit()
    c.close()
    conn.close()


def get_cursor_one(environment):
    conn=sqlite3.connect("{}.db".format(environment))
    cursor=conn.cursor()
#    print (cursor)
    return cursor, conn
def get_information():
    cursor,connection=get_cursor_one("shopping_list")

    cursor.execute('SELECT * FROM shopping_list')
    info=[]
    for row in cursor.fetchall():
        print(row)
        info.append(row)
        print(info)
    return info

def new_entry(title,description):
    cursor,connection=get_cursor_one("shopping_list")
    cursor.execute("INSERT INTO shopping_list(title,description) VALUES(?,?)", (title,description))
    connection.commit()
    return title,description
def delete_entry(title):
    cursor,connection=get_cursor_one("shopping_list")
    cursor.execute("DELETE FROM shopping_list WHERE title=?", (title,))
    connection.commit()

def delete_all():
    cursor,connection=get_cursor_one("shopping_list")
    cursor.execute("DELETE FROM shopping_list ")
    connection.commit()

#create_table()
#data_entry()
#get_information()
#new_entry("bread","for sandwiches")
#new_entry("wine","for party")
#delete_entry("wine")
#def get_item_list():
#    rows=get_information()
#    print(rows)
#    info=[]
#    for row in rows:
#        title=row[0]
#        description=row[1]
#        print(title,"--> ", description)
#        info

#get_information()
