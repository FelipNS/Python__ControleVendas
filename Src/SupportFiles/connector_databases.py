import mysql.connector
from random import randint
from tkinter import *
import tkinter.ttk as ttk
from time import sleep

def query_mysql():
    conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='acaiteria')
    cursor = conn.cursor()

    cursor.execute(f"SELECT id_previlegio FROM empregados WHERE id = {1}")
    id_prev = list(i for i in cursor)
    print(id_prev[0][0])
    cursor.close()

'''def query_mongo():
    for id in range(1, 17):
        mf.MongoCRUD().update_item({"_id": id}, {"seller": randint(1, 7)})'''


query_mysql()
