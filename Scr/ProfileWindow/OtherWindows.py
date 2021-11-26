from tkinter import *
import tkinter.ttk as ttk
import ProfileWindow.TkFuncProfile as tkp
from config.config import *

class WindowEdit:

    def __init__(self, id_user) -> None:
        self.root_edit = Tk()
        self.id_user = id_user
        CB = tkp.CommandsButtons(self.id_user, self.root_edit)
        self.root_edit.configure(background=DEFAUTL_BG_COLOR)

        self.label_name = ttk.Label(self.root_edit,
            text='Nome'
        )
        self.entry_name = ttk.Entry(self.root_edit,
            width=40,
            font=('Futura Gabriola Garamond', 10)
        )
        self.label_phone = ttk.Label(self.root_edit,
            text='Nº de celular'
        )
        self.entry_phone = ttk.Entry(self.root_edit,
            width=40,
            font=('Futura Gabriola Garamond', 10)
        )
        self.entry_phone.bind("<KeyRelease>", CB.format_number)
        self.label_email = ttk.Label(self.root_edit,
            text='Email'
        )
        self.entry_email = ttk.Entry(self.root_edit,
            width=40,
            font=('Futura Gabriola Garamond', 10)
        )
        self.button_save = Button(self.root_edit,
            text='Salvar',
            bg='#19c406',
            fg='white',
            command=lambda: CB.save_changes()
        )
        self.button_cancel = Button(self.root_edit,
            text='Cancelar',
            bg='#f50000',
            fg='white',
            command=lambda: CB.return_profile()
        )

        self.root_edit.eval(DEFAULT_WINDOW_POSITION)

        self.styles = ttk.Style()
        self.styles.configure('.', background='#ff80ff')
        self.styles.configure('TLabel', font=('Futura Gabriola Garamond', 10))

        self.label_name.grid(row=0, column=0, columnspan=2, padx=(20,20), pady=(20, 0), sticky=W)
        self.entry_name.grid(row=1, column=0, columnspan=2, padx=(20,20), pady=(0,10), sticky=W)
        self.label_phone.grid(row=2, column=0, columnspan=2, padx=(20,20), sticky=W)
        self.entry_phone.grid(row=3, column=0, columnspan=2, padx=(20,20), pady=(0,10), sticky=W)
        self.label_email.grid(row=4, column=0, columnspan=2, padx=(20,20), sticky=W)
        self.entry_email.grid(row=5, column=0, columnspan=2, padx=(20,20), pady=(0,10), sticky=W)
        self.button_save.grid(row=6, column=0, padx=(20,5), pady=(0,20), sticky='we')
        self.button_cancel.grid(row=6, column=1, padx=(5,20), pady=(0,20), sticky='we')


        self.entrys = (self.entry_name, self.entry_phone, self.entry_email)

    def return_entrys(self) -> tuple:
        return self.entrys

class WindowLevelTwo:

    def __init__(self, master: Tk) -> None:
        self.root = master

class WindowLevelThree:

    def __init__(self, master: Tk) -> None:
        self.root = master
