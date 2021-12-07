import SheetWindow.MongoFuncSheet as mf
import ProfileWindow as pw
from tkinter import *
import tkinter.messagebox

class CommandButtons:
    
    def __init__(self, **kargs) -> None:
        """Define commands to buttons OK, CLEAR and CLOSE.
        """
        self.kargs = kargs

    def clear_widgets(self):
        for frame in self.kargs['window'].children.values():
            for widget in frame.children.values():
                match widget.winfo_class():
                    case 'TEntry':
                        widget.delete(0, END)
                    case 'TCombobox':
                        widget.delete(0, END)
                    case 'Listbox':
                        widget.selection_clear(0, END)
                    case 'Labelframe':
                        for i in widget.children.values():
                            i.delete("1.0", END)
                    case _:
                        pass
    
    def close_window(self, id_user):
        self.kargs['window'].destroy()
        pw.ProfileApp(id_user)

    def save_sheet(self, json_sheet: dict):
        mf.MongoCRUD().insert_item(json_sheet)
        self.clear_widgets()
        tkinter.messagebox.showinfo(title='Comanda adicionada', message='Comanda adicionada com sucesso!')

