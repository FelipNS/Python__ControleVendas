from tkinter import *
import tkinter.ttk as ttk
import ProfileWindow.TkFuncProfile as tkf
import ProfileWindow.OtherWindows as ow
from PIL import Image, ImageTk
from config.config import * 

class ProfileApp(Tk):

    def __init__(self, id_user) -> None:
        super().__init__()

        self.title('PERFIL')
        self.configure(bg=PRIMARY_BG_COLOR)
        self.geometry('405x245')

        self.styles = ttk.Style()
        self.styles.configure('.', background=PRIMARY_BG_COLOR)
        self.styles.configure('TLabel', font=('Futura Gabriola Garamond', 10), foreground=DEFAULT_FG_COLOR)

        self.frame_sidebar = Frame(self,
            background=SECOND_BG_COLOR,
            class_='FrameSideBar'
        )
        img_logo = Image.open("Img/logo.jpg")
        img_logo = img_logo.resize((75, 43))
        img_tk_logo =  ImageTk.PhotoImage(img_logo)
        self.image_logo = ttk.Label(self.frame_sidebar,
            image=img_tk_logo,
            background=SECOND_BG_COLOR
        )
        img_gear = Image.open("Img/gear.jpg")
        img_gear = img_gear.resize((50, 50))
        img_tk_gear =  ImageTk.PhotoImage(img_gear)
        self.image_gear = ttk.Label(self.frame_sidebar,
            image=img_tk_gear,
            background=SECOND_BG_COLOR,
            cursor='hand2'
        )
        img_logout = Image.open("Img/logout.jpg")
        img_logout = img_logout.resize((50, 50))
        img_tk_logout =  ImageTk.PhotoImage(img_logout)
        self.image_logout = ttk.Label(self.frame_sidebar,
            image=img_tk_logout,
            background=SECOND_BG_COLOR,
            cursor='hand2'
        )
        
        self.image_gear.bind('<Button-1>', tkf.CommandsButtons.open_options)
        self.image_logout.bind('<Button-1>', tkf.CommandsButtons.exit_all)

        self.frame_sidebar.grid(row=0, column=0, sticky=NS)
        self.image_logo.pack(side=TOP, pady=(20, 0), fill=BOTH, anchor=CENTER)
        self.image_gear.pack(side=TOP, padx=(10, 10), pady=(25, 25), fill=BOTH, anchor=CENTER)
        self.image_logout.pack(side=BOTTOM, padx=(10, 10), pady=(0, 20), fill=BOTH, anchor=CENTER)

        WindowLevelOne(self, id_user)


class WindowLevelOne:

    def __init__(self, master: Tk, id_user) -> None:
        self.root = master
        self.id_user = id_user
        self.commands = tkf.CommandsButtons(self.id_user, self.root)

        self.frame_profile = Frame(self.root,
            background=PRIMARY_BG_COLOR,
            class_='FrameProfile'
        )         
        self.str_id = StringVar()
        self.label_id = ttk.Label(self.frame_profile,
            textvariable=self.str_id,
            class_='LabelID'
        )
        self.str_name = StringVar()
        self.label_name = ttk.Label(self.frame_profile,
            textvariable=self.str_name,
            class_='LabelName'
        )
        self.str_level = StringVar()
        self.label_level = ttk.Label(self.frame_profile,
            textvariable=self.str_level,
            class_='LabelLevel'
        )
        self.str_branch = StringVar()
        self.label_branch = ttk.Label(self.frame_profile,
            textvariable=self.str_branch,
            class_='LabelBranch'
        )
        self.button_new_sheet = ttk.Button(self.frame_profile,
            text='Cadastrar novas comandas',
            command=lambda: self.commands.open_sheet(),
            cursor='hand2'
        )
        
        self.frame_profile.grid(row=0, column=1, sticky=NS)
        self.label_id.grid(row=0, column=0, columnspan=2, sticky=W, padx=(20,20), pady=(20,10))
        self.label_name.grid(row=1, column=0, columnspan=2, sticky=W, padx=(20,20), pady=(0,10))
        self.label_level.grid(row=2, column=0, columnspan=2, sticky=W, padx=(20,20), pady=(0,10))
        self.label_branch.grid(row=3, column=0, columnspan=2, sticky=W, padx=(20,20), pady=(0,10))
        self.button_new_sheet.grid(row=4, column=0, columnspan=2, sticky=EW, padx=(20,20), pady=(0,10))
        
        datas = self.commands.query_profile()

        self.str_id.set(f'Nº DE REGISTRO: {datas["id"]}')
        self.str_name.set(f'NOME: {datas["name"]}')
        self.str_level.set(f'NÍVEL: {datas["level"]}')
        self.str_branch.set(f'FILIAL: {datas["branch"]}')


        match datas['level']:
            case 'NIVEL II':
                ow.WindowLevelTwo(self.root)
            case 'NIVEL III', _:
                ow.WindowLevelThree(self.root)

        self.root.eval(DEFAULT_WINDOW_POSITION)


        
        self.root.mainloop()