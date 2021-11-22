from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import Calendar
from datetime import datetime
from PIL import Image, ImageTk
from time import sleep
from Scr.SheetWindow.main_window import MainApp
import mysql.connector

class ProfileApp(Tk):

    def __init__(self,id_user) -> None:
        super().__init__()

        self.title('PERFIL')
        self.configure(bg='#ff80ff')

        WidgetsProfile(self, id_user)

        ProfileApp.set_geometry(self)

        self.styles = ttk.Style()
        self.styles.configure('.', background='#ff80ff')
        self.styles.configure('TLabel', font=('Futura Gabriola Garamond', 10))

        self.mainloop()
    
    def set_geometry(master: Tk):
        master.update_idletasks()
        w = master.winfo_reqwidth()
        h = master.winfo_reqheight()
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        master.geometry(f'{w}x{h}+{x}+{y}')
        master.minsize(w, h)
        master.maxsize(w, h)

class WidgetsProfile:

    def __init__(self, master, id_user) -> None:
        self.root = master
        self.id_user = id_user

        self.str_id = StringVar()
        self.label_id = ttk.Label(self.root,
            textvariable=self.str_id
        )
        self.str_name = StringVar()
        self.label_name = ttk.Label(self.root,
            textvariable=self.str_name
        )
        self.str_level = StringVar()
        self.label_level = ttk.Label(self.root,
            textvariable=self.str_level
        )
        self.button_new_sheet = ttk.Button(self.root,
            text='Cadastrar novas comandas',
            command=lambda: self._open_sheet()
        )

        self.frame_search = ttk.Frame(self.root)
        self.button_start = ttk.Button(self.frame_search,
            text='DE',
            command=lambda: self._open_calendar_start()
        )
        self.str_start = StringVar()
        self.label_start = ttk.Label(self.frame_search,
            textvariable=self.str_start
        )
        self.calendar_start = Calendar(self.frame_search, 
            selectmode='day', 
            locate='pt_BR', 
            firstweekday='sunday',
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day
        )
        self.calendar_start.bind('<<CalendarSelected>>', self.select_date)
        self.button_end = ttk.Button(self.frame_search,
            text='ATÉ',
            command=lambda: self._open_calendar_end()
        )
        self.str_end = StringVar()
        self.label_end = ttk.Label(self.frame_search,
            textvariable=self.str_end
        )
        self.calendar_end = Calendar(self.frame_search, 
            selectmode='day', 
            locate='pt_BR', 
            firstweekday='sunday',
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day
        )
        self.calendar_end.bind('<<CalendarSelected>>', self.select_date)
        
        self.label_id.grid(row=0, column=0, columnspan=2, sticky=W, padx=(20,20), pady=(20,10))
        self.label_name.grid(row=1, column=0, columnspan=3, sticky=W, padx=(20,20), pady=(0,10))
        self.label_level.grid(row=2, column=0, columnspan=3, sticky=W, padx=(20,20), pady=(0,10))
        self.button_new_sheet.grid(row=3, column=0, columnspan=3, sticky='we', padx=(20,20), pady=(0,10))

        self.frame_search.grid(row=4, column=0, columnspan=3, sticky='we', padx=(20,20), pady=(0,20))
        self.button_start.grid(row=0, column=0, padx=(20,10), pady=(0,5))
        self.button_end.grid(row=0, column=1, padx=(10,20), pady=(0,5))
        self.label_start.grid(row=1, column=0, padx=(20,10), pady=(0,20))
        self.label_end.grid(row=1, column=1, padx=(10,20), pady=(0,20))

        self._colect_profile()

    def _colect_profile(self):
        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='acaiteria')

        cursor = self.conn.cursor()
        cursor.execute(f'SELECT E.id, E.primeiro_nome, E.sobrenome, P.nome FROM empregados E JOIN previlegios P ON E.id_previlegio = P.id AND E.id = {self.id_user};')

        for id, first, last, level in cursor.fetchall():
            self.str_id.set(f'Nº DE REGISTRO: {id}')
            self.str_name.set(f'NOME: {first.upper()} {last.upper()}')
            self.str_level.set(f'NÍVEL: {level}')
        
    def _open_calendar_start(self):
        self.calendar_end.grid_forget()
        self.calendar_start.grid(row=2, column=0, columnspan=3)
        ProfileApp.set_geometry(self.root)
    
    def _open_calendar_end(self):
        self.calendar_start.grid_forget()
        self.calendar_end.grid(row=2, column=0, columnspan=3)
        ProfileApp.set_geometry(self.root)

    def select_date(self, evt=None):
        date_start = self.calendar_start.selection_get()
        date_end = self.calendar_end.selection_get()
        date_start = f'{date_start.day}/{date_start.month}/{date_start.year}'
        date_end = f'{date_end.day}/{date_end.month}/{date_end.year}'
        self.str_start.set(date_start)
        self.str_end.set(date_end)
        sleep(0.5)
        self.calendar_start.grid_forget()
        self.calendar_end.grid_forget()
        ProfileApp.set_geometry(self.root)


    def _open_sheet(self):
        self.root.destroy()
        MainApp()
