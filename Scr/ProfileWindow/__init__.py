from tkinter import *
import tkinter.ttk as ttk
import ProfileWindow.TkFuncProfile as tkf
from PIL import Image, ImageTk
from config.config import * 

class ProfileApp(Tk):

    def __init__(self, id_user: int) -> None:
        """Create root window, sidebar and loads profile widgets

        Args:
            id_user (int): ID user to load your profile.
        """
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
        img_logo = Image.open(r"Img\logo.jpg")
        img_logo = img_logo.resize((75, 43))
        img_tk_logo =  ImageTk.PhotoImage(img_logo)
        self.image_logo = ttk.Label(self.frame_sidebar,
                                    image=img_tk_logo,
                                    background=SECOND_BG_COLOR
                                    )
        
        img_menu = Image.open(r"Img\menu.jpg")
        img_menu = img_menu.resize((50, 50))
        img_tk_menu =  ImageTk.PhotoImage(img_menu)
        self.image_menu = ttk.Label(self.frame_sidebar,
                                    image=img_tk_menu,
                                    background=SECOND_BG_COLOR,
                                    cursor='hand2'
                                    )
        
        img_logout = Image.open(r"Img\logout.jpg")
        img_logout = img_logout.resize((50, 50))
        img_tk_logout =  ImageTk.PhotoImage(img_logout)
        self.image_logout = ttk.Label(self.frame_sidebar,
                                      image=img_tk_logout,
                                      background=SECOND_BG_COLOR,
                                      cursor='hand2'
                                      )
        self.image_menu.bind('<Button-1>', tkf.CommandsButtons.open_options)
        self.image_logout.bind('<Button-1>', tkf.CommandsButtons.exit_all)

        self.frame_sidebar.grid(row=0, column=0, sticky=NS)
        self.image_logo.pack(side=TOP, pady=(20, 0), fill=BOTH, anchor=CENTER)
        self.image_menu.pack(side=TOP, padx=(10, 10), pady=(25, 25), fill=BOTH, anchor=CENTER)
        self.image_logout.pack(side=BOTTOM, padx=(10, 10), pady=(0, 20), fill=BOTH, anchor=CENTER)

        WindowLevelOne(self, id_user)


class WindowLevelOne:

    def __init__(self, master: Tk, id_user: int) -> None:
        """Create profile widgets

        Args:
            master (Tk): root window
            id_user (int): ID user to load your profile.
        """
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

        self.root.eval(DEFAULT_WINDOW_POSITION)
        
        self.root.mainloop()

class WindowOption:
    def __init__(self, id:int, root: Tk) -> None:
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
                                         text='EDITAR DADOS PESSOAIS',
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
        self.label_export_data = ttk.Label(self.frame_option,
                                           width=40,
                                           text='EXPORTAR COMANDAS',
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
        self.label_edit_data.bind('<Button-1>', tkf.CommandsButtons.edit_datas)

        self.label_alter_account.bind('<Enter>', self.enter)
        self.label_alter_account.bind('<Leave>', self.leave)
        self.label_alter_account.bind('<Button-1>', tkf.CommandsButtons.return_login)

        self.label_export_data.bind('<Enter>', self.enter)
        self.label_export_data.bind('<Leave>', self.leave)
        self.label_export_data.bind('<Button-1>', tkf.CommandsButtons.export_window)

        self.label_return.bind('<Enter>', self.enter)
        self.label_return.bind('<Leave>', self.leave)
        self.label_return.bind('<Button-1>', tkf.CommandsButtons.return_profile)

        self.frame_option.grid(row=0, column=1, sticky=NS)
        self.label_edit_data.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), ipady=10, sticky=W)
        self.label_alter_account.grid(row=1, column=0, padx=(20, 0), ipady=10, sticky=W)
        if tkf.CommandsButtons(id, root).get_id_privilege_level() in (3, 4):
            self.label_export_data.grid(row=2, column=0, padx=(20, 0), ipady=10, sticky=W)
        self.label_return.grid(row=3, column=0, padx=(20, 0), pady=(0,20), ipady=10, sticky=W)

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
        CB = tkf.CommandsButtons(self.id_user, self.frame_edit)

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


class ExportWindow:
    def __init__(self, root: Tk, id: int) -> None:
        self.id = id
        self.CB = tkf.CommandsButtons(self.id, root)

        self.frame_export = Frame(root,
                                  bg=PRIMARY_BG_COLOR,
                                  class_='FrameExport'
                                  )
        self.button_export_excel = ttk.Button(self.frame_export, 
                                              text='Exportar dados para Excel',
                                              command=lambda: self.CB.export_to_excel()
                                              )
        self.button_export_pdf = ttk.Button(self.frame_export,
                                            text='Exportar para um relatório em PDF',
                                            command=lambda: self.CB.export_to_pdf()
                                            )
        self.button_return = ttk.Button(self.frame_export,
                                        text='Retornar',
                                        command=lambda: self.CB.open_options()
                                        )
        self.frame_export.grid(row=0, column=1, sticky=NS)
        self.button_export_excel.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky=EW)
        self.button_export_pdf.grid(row=1, column=0, padx=(20, 20), pady=(10, 10), sticky=EW)
        self.button_return.grid(row=2, column=0, padx=(20,20), pady=(0,20), sticky=EW)