from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
import SheetWindow as sw
import ProfileWindow as pw

class CommandsButtons:

    def __init__(self, id_user, master: Tk) -> None:
        self.master = master
        globals()['id_user']  = id_user
        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='acaiteria', port='3306')
        self.cursor = self.conn.cursor()

    def query_profile(self) -> dict:

        self.cursor.execute(f'SELECT E.*, P.nome FROM empregados E INNER JOIN previlegios P ON E.id_previlegio = P.id AND E.id = {globals()["id_user"]};')
        self.dict_datas = dict()

        for id, id_priv, first, last, nr_phone, email, level in self.cursor.fetchall():
            self.dict_datas['id'] = id
            self.dict_datas['id_priv'] = id_priv 
            self.dict_datas['name'] = f'{first.upper()} {last.upper()}'
            self.dict_datas['level'] = level
            self.dict_datas['nr_phone'] = nr_phone
            self.dict_datas['email'] = email
        
        return self.dict_datas

    def edit_datas(self):
        self.master.destroy()
        self.root_edit = Tk()
        self.root_edit.configure(background='#ff80ff')

        self.label_name = ttk.Label(self.root_edit,
            text='Nome'
        )
        self.entry_name = Entry(self.root_edit,
        )
        self.label_phone = ttk.Label(self.root_edit,
            text='Nº de celular'
        )
        self.entry_phone = Entry(self.root_edit,
        )
        self.entry_phone.bind("<KeyRelease>", self._format_number)
        self.label_email = ttk.Label(self.root_edit,
            text='Email'
        )
        self.entry_email = Entry(self.root_edit,
        )
        self.button_save = Button(self.root_edit,
            text='Salvar',
            bg='#19c406',
            fg='white',
            command=lambda: self._save_changes()
        )
        self.button_cancel = Button(self.root_edit,
            text='Cancelar',
            bg='#f50000',
            fg='white',
            command=lambda: self._return_profile()
        )

        pw.ProfileApp.set_geometry(self.root_edit)

        self.styles = ttk.Style()
        self.styles.configure('.', background='#ff80ff')
        self.styles.configure('TLabel', font=('Futura Gabriola Garamond', 10))

        datas_profile = self.query_profile()

        name = datas_profile['name'].title()
        phone = list(datas_profile['nr_phone'])
        insert_char = ((0, '('), (3, ')'), (4, ' '), (6, ' '), (11, '-'))
        for i in insert_char:
            phone.insert(i[0], i[1])
        number = ''
        for i in phone:
            number += i
        self.entry_name.insert(0, name) 
        self.entry_phone.insert(0, number)
        self.entry_email.insert(0, datas_profile['email'])

        self.label_name.grid(row=0, column=0, padx=(20,20), pady=(20,10), sticky=W)
        self.entry_name.grid(row=1, column=0, padx=(20,20), pady=(0,10), sticky=W)
        self.entry_phone.grid(row=2, column=0, padx=(20,20), pady=(0,10), sticky=W)
        self.entry_email.grid(row=3, column=0, padx=(20,20), pady=(0,10), sticky=W)
        self.button_save.grid(row=4, column=0, padx=(20,20), pady=(0,10), sticky=W)
        self.button_cancel.grid(row=5, column=0, padx=(20,20), pady=(0,20), sticky=W)

    def _format_number(self, evt):
        ignore_key = list(i for i in range(32,256) if not i in range(48,58))       
        number = self.entry_phone.get()
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
            self.entry_phone.delete(0, END)
            self.entry_phone.insert(0, number_for)
        elif evt.keysym_num in ignore_key:
            if len(number) == 1:
                self.entry_phone.delete(0, END)
            else:
                number.pop()
                for i in number:
                    number_for += i
                self.entry_phone.delete(0, END)
                self.entry_phone.insert(0, number_for)

    def _save_changes(self):
        name = self.entry_name.get()
        name = name.title().split(' ')
        first_name = name[0]
        last_name = name[1]
        for i in name[2::]:
            last_name += f' {i}'
        phone = self.entry_phone.get()
        number = ''
        for i in phone:
            if i.isnumeric():
                number += str(i)
        email = self.entry_email.get()
        sql = f'UPDATE empregados SET primeiro_nome = "{first_name}", sobrenome = "{last_name}", nr_celular = "{number}", email = "{email}" WHERE id = {globals()["id_user"]}'
        self.cursor.execute(sql)
        self.conn.commit()

        self.root_edit.destroy()
        pw.ProfileApp(globals()['id_user'])

    def _return_profile(self):
        self.root_edit.destroy()
        pw.ProfileApp(globals()['id_user'])

    def open_sheet(self, root):
        root.destroy()
        sw.MainApp(globals()['id_user'])

