from tkinter import *
from tkinter.messagebox import askyesno
import tkinter.ttk as ttk
import mysql.connector
from config.config import *
import SheetWindow as sw
import LoginWindow as lw
import ProfileWindow as pw
import ProfileWindow.OtherWindows as ow

class CommandsButtons:

    def __init__(self, id_user: int, master: Tk) -> None:
        """Connect to MySQL database and create global id_user and master variables 

        Args:
            id_user (int): ID user to load your profile.
            master (Tk): Root window
        """
        globals()["master"] = master
        globals()["id_user"] = id_user
        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='acaiteria', port='3306')
        self.cursor = self.conn.cursor()

    def query_profile(self) -> dict:
        """Colect user data in database 

        Returns:
            dict: Dict containing user data
        """
        self.cursor.execute(f'''SELECT E.id, E.primeiro_nome, E.sobrenome, E.nr_celular, E.email, P.nome Nivel, C.nome Cidade
            FROM empregados E 
            INNER JOIN previlegios P ON E.id_previlegio = P.id
            INNER JOIN cidades C ON E.id_filial = C.id
            WHERE E.id = {globals()["id_user"]};''')
        dict_datas = dict()

        for id, first, last, nr_phone, email, level, branch in self.cursor.fetchall():
            dict_datas['id'] = id
            dict_datas['name'] = f'{first.upper()} {last.upper()}'
            dict_datas['nr_phone'] = nr_phone
            dict_datas['email'] = email
            dict_datas['level'] = level
            dict_datas['branch'] = branch.upper()
        return dict_datas

    def edit_datas(self) -> None:
        """Open the editing frame 
        """
        datas_profile = CommandsButtons(globals()["id_user"], globals()["master"]).query_profile()
        name = datas_profile['name'].title()
        phone = list(datas_profile['nr_phone'])
        insert_char = ((0, '('), (3, ')'), (4, ' '), (6, ' '), (11, '-'))
        for i in insert_char:
            phone.insert(i[0], i[1])
        number = ''
        for i in phone:
            number += i
        
        #CREATE WINDOW's EDIT
        CommandsButtons.__switch_pages('FrameOption')
        if globals()["master"].master != None:
            try:
                win_edit = ow.WindowEdit(globals()["id_user"], globals()["master"].master)
            except:
                win_edit = ow.WindowEdit(globals()["id_user"], globals()["master"])
        else:
            win_edit = ow.WindowEdit(globals()["id_user"], globals()["master"])
        entrys = globals()['entrys'] = win_edit.return_entrys()
        entry_name = entrys[0]
        entry_phone = entrys[1]
        entry_email = entrys[2]
        entry_name.insert(0, name)
        entry_phone.insert(0, number)
        entry_email.insert(0, datas_profile['email'])

    def format_number(self, evt):
        """Event active whenever a key is pressed

        Args:
            evt (tk.Event): Don't matter
        """
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

    def save_changes(self) -> None:
        """Update database
        """
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
        sql = f'UPDATE empregados SET primeiro_nome = "{first_name}", sobrenome = "{last_name}", nr_celular = "{number}", email = "{email}" WHERE id = {globals()["id_user"]}'
        self.cursor.execute(sql)
        self.conn.commit()
        self.return_profile()

    def return_profile(self) -> None:
        """Return profile frame
        """
        CommandsButtons.__switch_pages('FrameEdit')
        CommandsButtons.__switch_pages('FrameOption')
        if globals()["master"].master != None:
            try:
                pw.WindowLevelOne(globals()["master"].master, globals()["id_user"])
            except:
                pw.WindowLevelOne(globals()["master"], globals()["id_user"])
        else:
            pw.WindowLevelOne(globals()["master"], globals()["id_user"])

    def return_login(self) -> None:
        """Destroy profile window and open login window
        """
        try:
            globals()["master"].master.destroy()
        except:
            globals()["master"].destroy()

        lw.MainLogin()
    
    def open_options(self) -> None:
        """Open option frame
        """
        CommandsButtons.__switch_pages('FrameProfile')
        CommandsButtons.__switch_pages('FrameEdit')
        if globals()["master"].master != None:
            try:
                ow.WindowOption(globals()["master"].master)
            except:
                ow.WindowOption(globals()["master"])
        else:
            ow.WindowOption(globals()["master"])

    def open_sheet(self) -> None:
        """Destroy profile window and open sheet window
        """
        try:
            globals()["master"].master.destroy()
        except:
            globals()["master"].destroy()

        sw.MainApp(globals()["id_user"])
    
    def exit_all(self) -> None:
        """Close app
        """
        if askyesno('FAZER LOGOUT', f'Deseja realmente fechar do programa?'):
            try:
                globals()["master"].master.destroy()
            except:
                globals()["master"].destroy()

    def __switch_pages(frame_class: Frame) -> None:
        """Forget grid of a frame before create the new frame

        Args:
            frame_class (tk.Frame): Frame that will destroy
        """
        try:
            for w in globals()["master"].master.children.values():
                if w.winfo_class() == frame_class:
                    for wid in w.children.values():
                        wid.grid_forget()
        except:
            for w in globals()["master"].children.values():
                if w.winfo_class() == frame_class:
                    for wid in w.children.values():
                        wid.grid_forget()