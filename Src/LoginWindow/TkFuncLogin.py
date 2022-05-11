from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import askyesno, showinfo
from ProfileWindow import ProfileApp
from config.config import *
import mysql.connector

class AcessDB:

    def __init__(self, master: Tk) -> None:
        """Create connect with MySQL database

        Args:
            master (Tk): Tk object root 
        """
        self.root = master
        self.conn = mysql.connector.connect(host=DB_HOST,
                                            user=DB_USER,
                                            password=DB_PWD,
                                            database=DB_NAME)

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