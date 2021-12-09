from tkinter import *
import tkinter.ttk as ttk
import ProfileWindow.TkFuncProfile as tkp
from config.config import *

class WindowOption:
    def __init__(self, root: Tk) -> None:
        """Create option frame in root window

        Args:
            root (Tk): root window
        """
        self.frame_option = Frame(root,
            background=PRIMARY_BG_COLOR,
            class_='FrameOption'
        )
        self.label_edit_data = ttk.Label(self.frame_option,
            width=40,
            text='EDITAR DADOS',
            background=PRIMARY_BG_COLOR,
            foreground=DEFAULT_FG_COLOR,
            cursor='hand2'
        )
        self.label_alter_account = ttk.Label(self.frame_option,
            width=40,
            text='ALTERAR CONTA',
            background=PRIMARY_BG_COLOR,
            foreground=DEFAULT_FG_COLOR,
            cursor='hand2'
        )
        self.label_return = ttk.Label(self.frame_option,
            width=40,
            text='VOLTAR AO PERFIL',
            background=PRIMARY_BG_COLOR,
            foreground=DEFAULT_FG_COLOR,
            cursor='hand2'
        )

        self.label_edit_data.bind('<Enter>', self.enter)
        self.label_edit_data.bind('<Leave>', self.leave)
        self.label_edit_data.bind('<Button-1>', tkp.CommandsButtons.edit_datas)

        self.label_alter_account.bind('<Enter>', self.enter)
        self.label_alter_account.bind('<Leave>', self.leave)
        self.label_alter_account.bind('<Button-1>', tkp.CommandsButtons.return_login)

        self.label_return.bind('<Enter>', self.enter)
        self.label_return.bind('<Leave>', self.leave)
        self.label_return.bind('<Button-1>', tkp.CommandsButtons.return_profile)

        self.frame_option.grid(row=0, column=1, sticky=NS)
        self.label_edit_data.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), ipady=10, sticky=W)
        self.label_alter_account.grid(row=1, column=0, padx=(20, 0), ipady=10, sticky=W)
        self.label_return.grid(row=2, column=0, padx=(20, 0), pady=(0,20), ipady=10, sticky=W)

        root.eval(DEFAULT_WINDOW_POSITION)
    
    def enter(self, event):
        """Event active when mouse is over label.

        Args:
            event (tk.Event): Don't matter
        """
        event.widget.configure(background=SECOND_BG_COLOR)

    def leave(self, event):
        """Event active when mouse leave label

        Args:
            event (tk.Event): Don't matter
        """
        event.widget.configure(background=PRIMARY_BG_COLOR)


class WindowEdit:
    def __init__(self, id_user: int, root: Tk) -> None:
        """Create frame to user modify your datas 

        Args:
            id_user (int): ID user to load your profile.
            root (Tk): Root window
        """
        self.frame_edit = Frame(root,
            bg=PRIMARY_BG_COLOR,
            class_='FrameEdit'
        )
        self.id_user = id_user
        CB = tkp.CommandsButtons(self.id_user, self.frame_edit)

        self.label_name = ttk.Label(self.frame_edit,
            text='Nome'
        )
        self.entry_name = ttk.Entry(self.frame_edit,
            width=40,
            font=('Futura Gabriola Garamond', 10)
        )
        self.label_phone = ttk.Label(self.frame_edit,
            text='Nº de celular'
        )
        self.entry_phone = ttk.Entry(self.frame_edit,
            width=40,
            font=('Futura Gabriola Garamond', 10)
        )
        self.entry_phone.bind("<KeyRelease>", CB.format_number)
        self.label_email = ttk.Label(self.frame_edit,
            text='Email'
        )
        self.entry_email = ttk.Entry(self.frame_edit,
            width=40,
            font=('Futura Gabriola Garamond', 10)
        )
        self.button_save = Button(self.frame_edit,
            text='Salvar',
            bg='#19c406',
            fg='white',
            command=lambda: CB.save_changes(),
            cursor='hand2'
        )
        self.button_cancel = Button(self.frame_edit,
            text='Cancelar',
            bg='#f50000',
            fg='white',
            command=lambda: CB.return_profile(),
            cursor='hand2'
        )

        self.styles = ttk.Style()
        self.styles.configure('.', background=PRIMARY_BG_COLOR)
        self.styles.configure('TLabel', font=('Futura Gabriola Garamond', 10), foreground=DEFAULT_FG_COLOR)
        
        self.frame_edit.grid(row=0, column=1, sticky=NS)
        self.label_name.grid(row=0, column=0, columnspan=2, padx=(20,20), pady=(20, 0), sticky=W)
        self.entry_name.grid(row=1, column=0, columnspan=2, padx=(20,20), pady=(0,10), sticky=W)
        self.label_phone.grid(row=2, column=0, columnspan=2, padx=(20,20), sticky=W)
        self.entry_phone.grid(row=3, column=0, columnspan=2, padx=(20,20), pady=(0,10), sticky=W)
        self.label_email.grid(row=4, column=0, columnspan=2, padx=(20,20), sticky=W)
        self.entry_email.grid(row=5, column=0, columnspan=2, padx=(20,20), pady=(0,10), sticky=W)
        self.button_save.grid(row=6, column=0, padx=(20,5), pady=(0,20), sticky=EW)
        self.button_cancel.grid(row=6, column=1, padx=(5,20), pady=(0,20), sticky=EW)

        root.eval(DEFAULT_WINDOW_POSITION)

        self.entrys = (self.entry_name, self.entry_phone, self.entry_email)

    def return_entrys(self) -> tuple:
        """Return tuple with entry widgets

        Returns:
            tuple: Contains entry widgets
        """
        return self.entrys


