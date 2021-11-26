from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
from config.config import *
import SheetWindow as sw
import LoginWindow as lw
import ProfileWindow as pw
import ProfileWindow.OtherWindows as ow

class CommandsButtons:

    def __init__(self, id_user, master: Tk) -> None:
        self.master = master
        self.id_user = id_user
        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='acaiteria', port='3306')
        self.cursor = self.conn.cursor()

    def query_profile(self) -> dict:
        self.cursor.execute(f'SELECT E.*, P.nome FROM empregados E INNER JOIN previlegios P ON E.id_previlegio = P.id AND E.id = {self.id_user};')
        dict_datas = dict()

        for id, id_priv, first, last, nr_phone, email, level in self.cursor.fetchall():
            dict_datas['id'] = id
            dict_datas['id_priv'] = id_priv 
            dict_datas['name'] = f'{first.upper()} {last.upper()}'
            dict_datas['level'] = level
            dict_datas['nr_phone'] = nr_phone
            dict_datas['email'] = email
        return dict_datas

    def edit_datas(self):
        self.master.destroy()
        datas_profile = self.query_profile()
        name = datas_profile['name'].title()
        phone = list(datas_profile['nr_phone'])
        insert_char = ((0, '('), (3, ')'), (4, ' '), (6, ' '), (11, '-'))
        for i in insert_char:
            phone.insert(i[0], i[1])
        number = ''
        for i in phone:
            number += i
        
        #CREATE WINDOW's EDIT
        win_edit = ow.WindowEdit(self.id_user)
        entrys = globals()['entrys'] = win_edit.return_entrys()
        entry_name = entrys[0]
        entry_phone = entrys[1]
        entry_email = entrys[2]
        entry_name.insert(0, name)
        entry_phone.insert(0, number)
        entry_email.insert(0, datas_profile['email'])

    def format_number(self, evt):
        entrys = globals()['entrys']
        entry_phone = entrys[1]

        ignore_key = list(i for i in range(32,256) if not i in range(48,58))
        number = entry_phone.get()
        number = list(number)
        number_for = ''
        if evt.keysym.isnumeric():
            match len(number):
                case 1:
                    number.insert(0, '(')
                case 4:
                    number.insert(3, ')')
                    number.insert(4, ' ')
                case 7:
                    number.insert(6, ' ')
                case 12:
                    number.insert(11, '-')
            for i in number:
                number_for += i
            entry_phone.delete(0, END)
            entry_phone.insert(0, number_for)
        elif evt.keysym_num in ignore_key:
            if len(number) == 1:
                entry_phone.delete(0, END)
            else:
                number.pop()
                for i in number:
                    number_for += i
                entry_phone.delete(0, END)
                entry_phone.insert(0, number_for)

    def save_changes(self):
        entrys = globals()['entrys']
        entry_name = entrys[0]
        entry_phone = entrys[1]
        entry_email = entrys[2]

        name = entry_name.get()
        name = name.title().split(' ')
        first_name = name[0]
        last_name = name[1]
        for i in name[2::]:
            last_name += f' {i}'
        phone = entry_phone.get()
        number = ''
        for i in phone:
            if i.isnumeric():
                number += str(i)
        email = entry_email.get()
        sql = f'UPDATE empregados SET primeiro_nome = "{first_name}", sobrenome = "{last_name}", nr_celular = "{number}", email = "{email}" WHERE id = {self.id_user}'
        self.cursor.execute(sql)
        self.conn.commit()
        self.master.destroy()
        pw.ProfileApp(self.id_user)

    def return_profile(self):
        self.master.destroy()
        pw.ProfileApp(self.id_user)

    def return_login(self):
        self.master.destroy()
        lw.MainLogin()

    def open_sheet(self):
        self.master.destroy()
        sw.MainApp(self.id_user)
    
    def exit_all(self):
        self.master.destroy()
    




