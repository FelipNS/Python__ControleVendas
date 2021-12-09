from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import askyesno, showinfo
from ProfileWindow import ProfileApp
from config.config import *
import mysql.connector

class MainLogin(Tk):

    def __init__(self) -> None:
        """Create root window  
        """
        super().__init__()

        self.title('LOGIN')
        self.configure(bg=PRIMARY_BG_COLOR)
  
        WidgetsLogin(self)

        self.update_idletasks()
        self.eval(DEFAULT_WINDOW_POSITION)

        self.styles = ttk.Style()
        self.styles.configure('TLabel', background=PRIMARY_BG_COLOR, foreground=DEFAULT_FG_COLOR)
        self.mainloop()


class WidgetsLogin:

    def __init__(self, master: Tk) -> None:
        """Create window windets

        Args:
            master (Tk): root window Tk object 
        """
        self.root = master

        self.label_login = ttk.Label(self.root, 
            text='LOGIN', 
            font=('Futura Gabriola Garamond', 18, "bold"),
            width=15,
            anchor=CENTER,
        )
        self.label_username = ttk.Label(self.root, 
            text='USUÁRIO', 
            font=('Futura Gabriola Garamond', 12)
        )
        self.entry_username = ttk.Entry(self.root
        )
        self.label_password = ttk.Label(self.root, 
            text='SENHA', 
            font=('Futura Gabriola Garamond', 12)
        )
        self.entry_password = ttk.Entry(self.root,
            show='*'
        )
        self.value_checkbox = BooleanVar()
        self.checkbox_hidden_pwd = Checkbutton(self.root,
            background=PRIMARY_BG_COLOR,
            foreground=DEFAULT_FG_COLOR,
            activebackground=PRIMARY_BG_COLOR,
            activeforeground=DEFAULT_FG_COLOR,
            selectcolor=PRIMARY_BG_COLOR,
            text='Mostrar senha',
            takefocus=False,
            variable=self.value_checkbox,
            command=lambda: self._hidden_show_pwd()
        )
        self.button_ok = ttk.Button(self.root, 
            text='ENTRAR',
            command=lambda: AcessDB(self.root).query_name(self.entry_username.get(), self.entry_password.get()),
            takefocus=False,
            cursor='hand2'
        )
        self.button_exit = ttk.Button(self.root,
            text='SAIR',
            command=lambda: self.close_app(),
            takefocus=False,
            cursor='hand2'
        )

        self.label_login.grid(row=0, column=0, columnspan=3, sticky=EW,padx=(50,50), pady=(10, 10))
        self.label_username.grid(row=1, column=0, columnspan=3, sticky=W, padx=(50,50))
        self.entry_username.grid(row=2, column=0, columnspan=3, sticky=EW, padx=(50,50), pady=(0, 10))
        self.label_password.grid(row=3, column=0, columnspan=3, sticky=W, padx=(50,50))
        self.entry_password.grid(row=4, column=0, columnspan=3, sticky=EW, padx=(50,50))
        self.checkbox_hidden_pwd.grid(row=5, column=0, sticky=W, padx=(50,50), pady=(0, 10))
        self.button_ok.grid(row=6, column=0, columnspan=3, sticky=EW, padx=(50,50), pady=(0, 10))
        self.button_exit.grid(row=7, column=0, columnspan=3, sticky=EW, padx=(50,50), pady=(0, 10))
    
    def _hidden_show_pwd(self) -> None:
        """Show or hidden password
        """
        if self.value_checkbox.get():
            self.entry_password.config(show='')
        else:
            self.entry_password.config(show='*')
    
    def close_app(self) -> None:
        """Destroy root window
        """
        if askyesno('SAIR', 'Deseja mesmo sair do programa?'):
            self.root.destroy()


class AcessDB:

    def __init__(self, master: Tk) -> None:
        """Create connect with MySQL database

        Args:
            master (Tk): Tk object root 
        """
        self.root = master
        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='acaiteria')

    def query_name(self, user: str, password: str) -> None:
        """query database looking for an existing user with past password

        Args:
            user (str): entry_username value
            password (str): entry_password value
        """
        cursor = self.conn.cursor(buffered=True)
        cursor.execute(f'SELECT id_empregado FROM login_empregados WHERE BINARY nome_usuario = "{user}" AND BINARY senha_usuario = "{password}"')

        if cursor.rowcount == 0:
            showinfo('USUÁRIO OU SENHA INCORRETA!', 'USUÁRIO OU SENHA INCORRETA!')
        else:
            id_user = cursor.fetchone()[0]

            cursor.close()
            self.conn.close()
            self.root.destroy()
            ProfileApp(id_user)