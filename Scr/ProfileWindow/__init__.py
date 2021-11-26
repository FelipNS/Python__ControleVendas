from tkinter import *
import tkinter.ttk as ttk
import ProfileWindow.TkFuncProfile as tkf
import ProfileWindow.OtherWindows as ow
from config.config import * 

class ProfileApp(Tk):

    def __init__(self, id_user) -> None:
        super().__init__()

        self.title('PERFIL')
        self.configure(bg=DEFAUTL_BG_COLOR)

        WindowLevelOne(self, id_user)

        self.eval(DEFAULT_WINDOW_POSITION)

        self.styles = ttk.Style()
        self.styles.configure('.', background='#ff80ff')
        self.styles.configure('TLabel', font=('Futura Gabriola Garamond', 10))

        self.mainloop()
class WindowLevelOne:

    def __init__(self, master: Tk, id_user) -> None:
        self.root = master
        self.id_user = id_user
        self.commands = tkf.CommandsButtons(self.id_user, self.root)

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
            command=lambda: self.commands.open_sheet()
        )
        self.button_edit_data = ttk.Button(self.root,
            text='Editar dados',
            command=lambda: self.commands.edit_datas()
        )
        self.button_alter_account = ttk.Button(self.root,
            text='Alterar conta',
            command=lambda: self.commands.return_login()
        )
        self.button_logout = ttk.Button(self.root,
            text='SAIR',
            command=lambda: self.commands.exit_all()
        )
        
        self.label_id.grid(row=0, column=0, columnspan=2, sticky=W, padx=(20,20), pady=(20,10))
        self.label_name.grid(row=1, column=0, columnspan=3, sticky=W, padx=(20,20), pady=(0,10))
        self.label_level.grid(row=2, column=0, columnspan=3, sticky=W, padx=(20,20), pady=(0,10))
        self.button_new_sheet.grid(row=3, column=0, columnspan=3, sticky='we', padx=(20,20), pady=(0,10))
        self.button_edit_data.grid(row=4, column=0, columnspan=3, sticky='we', padx=(20,20), pady=(0,10))
        self.button_alter_account.grid(row=5, column=0, columnspan=3, sticky='we', padx=(20,20), pady=(0,10))
        self.button_logout.grid(row=6, column=0, columnspan=3, sticky='we', padx=(20,20), pady=(0,10))

        datas = self.commands.query_profile()

        self.str_id.set(f'Nº DE REGISTRO: {datas["id"]}')
        self.str_name.set(f'NOME: {datas["name"]}')
        self.str_level.set(f'NÍVEL: {datas["level"]}')

        match datas['level']:
            case 'NIVEL II':
                ow.WindowLevelTwo(self.root)
            case 'NIVEL III', _:
                ow.WindowLevelThree(self.root)
