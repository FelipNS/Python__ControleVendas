from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
import SheetWindow as sw

class CommandsButtons:

    def __init__(self) -> None:

        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='acaiteria')
        self.cursor = self.conn.cursor()

    def query_profile(self, id_user) -> dict:
        self.id_user = id_user

        self.cursor.execute(f'SELECT E.*, P.nome FROM empregados E INNER JOIN previlegios P ON E.id_previlegio = P.id AND E.id = {self.id_user};')
        self.dict_datas = dict()

        for id, id_priv, first, last, nr_phone, level in self.cursor.fetchall():
            self.dict_datas['id'] = id
            self.dict_datas['id_priv'] = id_priv 
            self.dict_datas['name'] = f'{first.upper()} {last.upper()}'
            self.dict_datas['level'] = level
            self.dict_datas['nr_phone'] = nr_phone

        return self.dict_datas        

    def open_sheet(self, root):
        root.destroy()
        sw.MainApp(self.id_user)

