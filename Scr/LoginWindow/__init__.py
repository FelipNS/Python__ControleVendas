from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from ProfileWindow import ProfileApp
import mysql.connector

class MainLogin(Tk):

    def __init__(self) -> None:
        super().__init__()

        self.title('LOGIN')
        self.configure(bg='#ff80ff')
  
        WidgetsLogin(self)

        self.update_idletasks()
        self.eval('tk::PlaceWindow . center')

        self.styles = ttk.Style()
        self.styles.configure('.', background='#ff80ff')

        self.mainloop()


class WidgetsLogin:

    def __init__(self, master: Tk) -> None:
        self.root = master

        self.label_login = ttk.Label(self.root, 
            text='LOGIN', 
            font=('Futura Gabriola Garamond', 18, "bold"),
            width=15,
            anchor=CENTER
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
            bg='#ff80ff',
            text='Mostrar senha',
            activebackground='#ff80ff',
            variable=self.value_checkbox,
            command=lambda: self._hidden_show_pwd()
        )
        self.button_ok = ttk.Button(self.root, 
            text='ENTRAR',
            command=lambda: AcessDB(self.root).query_name(self.entry_username.get(), self.entry_password.get())
        )

        self.label_login.grid(row=0, column=0, columnspan=3, sticky='we',padx=(50,50), pady=(10, 10))
        self.label_username.grid(row=1, column=0, columnspan=3, sticky=W, padx=(50,50))
        self.entry_username.grid(row=2, column=0, columnspan=3, sticky='we', padx=(50,50), pady=(0, 10))
        self.label_password.grid(row=3, column=0, columnspan=3, sticky=W, padx=(50,50))
        self.entry_password.grid(row=4, column=0, columnspan=3, sticky='we', padx=(50,50))
        self.checkbox_hidden_pwd.grid(row=5, column=0, sticky=W, padx=(50,50), pady=(0, 10))
        self.button_ok.grid(row=6, column=0, columnspan=3, sticky='we', padx=(50,50), pady=(0, 10))
    
    def _hidden_show_pwd(self):
        if self.value_checkbox.get():
            self.entry_password.config(show='')
            self.checkbox_hidden_pwd.config(text='Ocultar senha')
        else:
            self.entry_password.config(show='*')
            self.checkbox_hidden_pwd.config(text='Mostrar senha')


class AcessDB:

    def __init__(self, master) -> None:
        self.root = master
        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='acaiteria')

    def query_name(self, user, password):

        cursor = self.conn.cursor(buffered=True)
        cursor.execute(f'SELECT id_empregado FROM login_empregados WHERE BINARY nome_usuario = "{user}" AND BINARY senha_usuario = "{password}"')

        if cursor.rowcount == 0:
            showinfo('USUÁRIO OU SENHA INCORRETA!', 'USUÁRIO OU SENHA INCORRETA!')
        else:
            self.id_user = cursor.fetchone()[0]

            cursor.close()
            self.conn.close()
            self.root.destroy()
            ProfileApp(self.id_user)