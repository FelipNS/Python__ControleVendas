import SheetWindow.MongoFuncSheet as mf
from SheetWindow import *
import ProfileWindow as pw
from tkinter import *
import tkinter.ttk as ttk
from tkinter.messagebox import showwarning, showinfo

class CommandButtons:
    
    def __init__(self, **kargs) -> None:
        """Define commands to buttons OK, CLEAR and CLOSE.
        """
        self.kargs = kargs

    def clear_widgets(self) -> None:
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
    
    def close_window(self) -> None:
        self.kargs['window'].destroy()
        pw.ProfileApp(self.kargs['id_user'])

    def save_sheet(self, json_sheet: dict) -> None:
        mf.MongoFunctions().insert_item(json_sheet)
        self.clear_widgets()
        showinfo(title='Comanda adicionada', message='Comanda adicionada com sucesso!')
    
    def send_data(self, *widget_args) -> None:
        """Send data to save database
        """
        json_datas = self.__create_json(widget_args)
        if json_datas != None:
            full_json = {**json_datas, **widget_args[-1]}
            self.save_sheet(full_json) 
    
    def __create_json(self, *args) -> dict:
        """Format the data in json file

        Args:
            number_sheet (ttk.Entry): Value entry_sheet_number
            combo (ttk.Combobox): Value combobox_combo_name
            payment_method (ttk.Combobox): Value combobox_payment_option
            price (ttk.Entry): Value entry_price
            size (ttk.Combobox): Value combobox_size
            neighborhood (ttk.Combobox): Value entry_neighborhood
            obs (Text): Value textbox_obs

        Returns:
            dict: Dict containing data sheet
        """
        args = args[0]
        print(args)
        if self.__is_empty(args):
            showwarning('CAMPOS NÃO PREENCHIDOS', 'Exite um ou mais campos do cabeçalho em branco! Preencha-os e tente novamente.')
        else:
            json_sketch = {
                "n_comanda": int(args[0].get()),
                "combo": args[1].get(),
                "f_pagamento": args[2].get(),
                "preco": float(args[3].get()),
                "tamanho": int(args[4].get().split(' ')[0]) if int(args[4].get().split(' ')[0]) != 1 else 1000,
                "bairro": args[5].get(),
                "obs": args[6].get("1.0", END),
                "seller": self.kargs['id_user']
            }
            return json_sketch

    def __is_empty(self, *args) -> bool:
        """Verify if a widget is empty

        Returns:
            bool: Return true if one widget is empty
        """
        isEmpty = False
        args = args[0][:6]
        for i in args:
            print(i.winfo_class(), args.index(i))
            if i.get() == '':
                isEmpty = True
                break
        return isEmpty


