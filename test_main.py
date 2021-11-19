from tkinter import *
import tkinter.ttk as ttk
from MongoFunctions import *
from TkinterFunctions import *

class MainApp(Tk):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.title('Cadastro comandas')
        self.configure(bg='#f1cbff')
        
        """width= 640
        height = 720
        x = self.winfo_screenwidth()
        y = self.winfo_screenheight()
        pos_x = int((x/2) - (width/2))
        pos_y = int((y/2) - (height/2))
        self.geometry(f'{width}x{height}+{pos_x}+{pos_y}')"""
        
        Header(self)
        Additionals(self)
        ButtonAndObs(self)

        self.styles = ttk.Style()
        self.styles.configure('.', font=('Apple LiGothic', 10, "bold"))
        self.styles.configure('TLabel', background='#f1cbff')
        self.styles.configure('left.TLabel', width=24)
        self.styles.configure('right.TLabel', width=11, padding=[180,0,0,0], anchor=E)
        self.styles.configure('TFrame', background='#f1cbff')

        self.mainloop()

class Header:

    def __init__(self, master: Tk) -> None:
        self.root = master

        self.frame_header = ttk.Frame(self.root, 
            width=130, 
            height=30,
        )
        self.label_sheet_number = ttk.Label(self.frame_header, 
            text='Nº DA COMANDA: ', 
            style='left.TLabel'
        )
        self.entry_sheet_number = ttk.Entry(self.frame_header, 
            style='default.TEntry', 
            width=25
        )
        self.label_combo_name = ttk.Label(self.frame_header, 
            text='COMBO: ', 
            style='right.TLabel'
        )
        self.combobox_combo_name = ttk.Combobox(self.frame_header, 
            values=MongoReadCollection('dadosGerais').read_item('combos'), 
            width=22
        )
        self.label_payment_option = ttk.Label(self.frame_header, 
            text='FORMA DE PAGAMENTO: ', 
            style='left.TLabel'
        )
        self.combobox_payment_option = ttk.Combobox(self.frame_header, 
            values=MongoReadCollection('dadosGerais').read_item('payment_option'), 
            width=22
        )
        self.label_price = ttk.Label(self.frame_header, 
            text='VALOR (R$): ', 
            style='right.TLabel'
        )
        self.entry_price = ttk.Entry(self.frame_header, 
            style='default.TEntry', 
            width=25
        )
        self.label_size = ttk.Label(self.frame_header, 
            text='TAMANHO: ', 
            style='left.TLabel'
        )
        self.combobox_size = ttk.Combobox(self.frame_header, 
            values=MongoReadCollection('dadosGerais').read_item('size'), 
            width=22
        )
        self.label_neighborwood = ttk.Label(self.frame_header, 
            text='BAIRRO: ', 
            style='right.TLabel'
        )
        self.combobox_neighborwood = ttk.Combobox(self.frame_header, 
            values=MongoReadCollection('dadosGerais').read_item('neighborwood'), 
            width=22
        )

        
        self.frame_header.grid(row=0, rowspan=4, column=0, columnspan=5, padx=(20,20), pady=(20,20))
        self.label_sheet_number.grid(row=0, column=0, pady=(0,2))
        self.entry_sheet_number.grid(row=0, column=1, pady=(0,2))
        self.label_combo_name.grid(row=0, column=2, pady=(0,2))
        self.combobox_combo_name.grid(row=0, column=3, pady=(0,2))
        self.label_payment_option.grid(row=1, column=0, pady=(0,2))
        self.combobox_payment_option.grid(row=1, column=1, pady=(0,2))
        self.label_price.grid(row=1, column=2, pady=(0,2))
        self.entry_price.grid(row=1, column=3, pady=(0,2))
        self.label_size.grid(row=2, column=0, pady=(0,2))
        self.combobox_size.grid(row=2, column=1, pady=(0,2))
        self.label_neighborwood.grid(row=2, column=2, pady=(0,2))
        self.combobox_neighborwood.grid(row=2, column=3, pady=(0,2))


class Additionals:

    def __init__(self, master: Tk) -> None:
        self.root = master

        self.additionals_type = ['cereais', 'chocolates', 'coberturas', 'derivados do leite', 'diversos', 'frutas']

        for i in range(0,len(self.additionals_type)):
            self.list_itens = MongoReadCollection('adicionais').read_item(self.additionals_type[i])
            match i:
                case 0:
                    k = 0
                    start_row = 4
                    p= (20,0)
                case 1:
                    k = 1
                    start_row = 4
                    p= (20,0)
                case 2:
                    k = 2
                    start_row = 4
                    p= (20,0)
                case 3:
                    k = 3
                    start_row = 4
                    p= (20,20)
                case 4:
                    k = 0
                    start_row = 16
                    p= (20,0)
                case 5:
                    k = 1
                    start_row = 16
                    p= (20,0)
            globals()[f'frame_{self.additionals_type[i]}'] = ttk.Frame(self.root)
            globals()[f'scrollbar_{self.additionals_type[i]}'] = Scrollbar(globals()[f'frame_{self.additionals_type[i]}'],
                orient=VERTICAL
                )
            globals()[f'listbox_{self.additionals_type[i]}'] = Listbox(globals()[f'frame_{self.additionals_type[i]}'], 
                font=('Apple LiGothic', 10),
                selectmode=MULTIPLE, 
                exportselection=False,
                yscrollcommand=globals()[f'scrollbar_{self.additionals_type[i]}'].set
            )
            for j in range(0, len(self.list_itens)):
                globals()[f'listbox_{self.additionals_type[i]}'].insert(END, self.list_itens[j])

            globals()[f'label_{self.additionals_type[i]}'] = ttk.Label(globals()[f'frame_{self.additionals_type[i]}'], 
                text=self.additionals_type[i].upper()
            ).grid(row=0, column=0)

            globals()[f'frame_{self.additionals_type[i]}'].grid(row=start_row, column=k, rowspan=8, padx=p, pady=(0,20))
            globals()[f'listbox_{self.additionals_type[i]}'].grid(row=1, column=0)
            globals()[f'scrollbar_{self.additionals_type[i]}'].grid(row=1, rowspan=8, column=1, sticky=NS)
            globals()[f'scrollbar_{self.additionals_type[i]}'].config(command=globals()[f'listbox_{self.additionals_type[i]}'].yview)
    
    
class ButtonAndObs(Header, Additionals):

    def __init__(self, master: Tk) -> None:
        Header.__init__(self, master)
        Additionals.__init__(self, master)
    
        self.frame_buttons = ttk.Frame(self.root)
        self.button_ok = Button(self.frame_buttons, 
            text='OK', 
            width=15, 
            height=2, 
            background='lime',
            command=lambda: self.send_data()
        )
        self.button_close = Button(self.frame_buttons, 
            text='SAIR', 
            width=15, 
            height=2, 
            background='red',
            command=lambda: CommandButtons(window=self.root).close_window()
        )
        self.button_clear = Button(self.frame_buttons, 
            text='Limpar', 
            width=15, 
            height=2, 
            background='yellow',
            command=lambda: CommandButtons(window=self.root).clear_widgets()
        )
        self.label_obs = LabelFrame(self.frame_buttons, 
            text='Observações', 
            bg='#f1cbff', 
            font=('Apple LiGothic', 15)
        )
        self.textbox_obs = Text(self.label_obs, 
            width=52, 
            height=5,
            font=('Apple LiGothic', 10)
        )

        self.frame_buttons.grid(row=16, column=2, columnspan=2)
        self.button_ok.grid(row=1, column=0, padx=(20,0), pady=(0,20))
        self.button_clear.grid(row=1, column=1, padx=(10,10), pady=(0,20))
        self.button_close.grid(row=1, column=2, padx=(0,20), pady=(0,20))
        self.label_obs.grid(row=0, column=0, columnspan=3, padx=(20,20), pady=(0,20))
        self.textbox_obs.grid(row=0, column=0, rowspan=11)
    
    def send_data(self):
        json_datas = self._create_json(self.entry_sheet_number, self.combobox_combo_name, self.combobox_payment_option, self.entry_price, self.combobox_size, self.combobox_neighborwood)
        for i in self.additionals_type:
            json_datas[i] = self._create_dict_additionals(globals()[f'listbox_{i}'])
        CommandButtons(window=self.root).save_sheet(json_datas)
    
    def _create_json(self, number_sheet: ttk.Entry, combo: ttk.Combobox, payment_method: ttk.Combobox, price: ttk.Entry, size: ttk.Combobox, neighborwood: ttk.Combobox):
        json_sketch = {
            "n_comanda": number_sheet.get(),
            "combo": combo.get(),
            "f_pagamento": payment_method.get(),
            "preco": price.get(),
            "tamanho": size.get(),
            "bairro": neighborwood.get()
        }
        return json_sketch
    
    def _create_dict_additionals(self, listbox_name: Listbox):
        dict_temp = [listbox_name.get(i) for i in listbox_name.curselection()]

        return dict_temp


if __name__ == '__main__':
    MainApp()