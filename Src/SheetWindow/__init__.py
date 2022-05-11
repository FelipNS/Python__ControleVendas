from tkinter import *
import tkinter.ttk as ttk
import SheetWindow.MongoFuncSheet as mf
import SheetWindow.TkFuncSheet as tkf
from config.config import *

class MainApp(Tk):
    
    def __init__(self, id_user: int) -> None:
        """Create sheet root window

        Args:
            id_user (int): ID user to save sheet in your name.
        """
        super().__init__()
        
        self.title('Cadastro comandas')
        self.configure(bg=PRIMARY_BG_COLOR)

        ButtonAndObs(self, id_user)
        
        self.update_idletasks()
        self.eval(DEFAULT_WINDOW_POSITION)
        
        self.styles = ttk.Style()
        self.styles.configure('.', font=('Apple LiGothic', 10, "bold"))
        self.styles.configure('TLabel', background=PRIMARY_BG_COLOR, foreground=DEFAULT_FG_COLOR)
        self.styles.configure('left.TLabel', width=24)
        self.styles.configure('right.TLabel', width=11, padding=[180,0,0,0], anchor=E)
        self.styles.configure('TFrame', background=PRIMARY_BG_COLOR, foreground=DEFAULT_FG_COLOR)
        self.mainloop()


class Header:

    def __init__(self, master: Tk) -> None:
        """Header of window

        Args:
            master (Tk): Root window
        """
        self.root = master
        self.mong = mf.MongoFunctions()

        self.frame_header = ttk.Frame(self.root, 
                                      width=130, 
                                      height=30
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
                                                values=self.mong.read_item('combos', 'dadosGerais'), 
                                                width=22
                                                )
        self.label_payment_option = ttk.Label(self.frame_header, 
                                              text='FORMA DE PAGAMENTO: ', 
                                              style='left.TLabel'
                                              )
        self.combobox_payment_option = ttk.Combobox(self.frame_header, 
                                                    values=self.mong.read_item('payment_option', 'dadosGerais'), 
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
                                          values=self.mong.read_item('size', 'dadosGerais'), 
                                          width=22
                                          )
        self.label_neighborhood = ttk.Label(self.frame_header, 
                                            text='BAIRRO: ', 
                                            style='right.TLabel'
                                            )
        self.combobox_neighborhood = ttk.Combobox(self.frame_header, 
                                                  values=self.mong.read_item('neighborhood', 'dadosGerais'), 
                                                  width=22
                                                  )
        self.frame_header.grid(row=0, rowspan=4, column=0, columnspan=5, padx=(20,20), pady=(20,20))
        self.label_sheet_number.grid(row=0, column=0, pady=(0,2))
        self.entry_sheet_number.grid(row=0, column=1, pady=(0,2))
        self.label_combo_name.grid(row=0, column=2, pady=(0,2))
        self.combobox_combo_name.grid(row=0, column=3, padx=(0,10), pady=(0,2))
        self.label_payment_option.grid(row=1, column=0, pady=(0,2))
        self.combobox_payment_option.grid(row=1, column=1, pady=(0,2))
        self.label_price.grid(row=1, column=2, pady=(0,2))
        self.entry_price.grid(row=1, column=3, padx=(0,10), pady=(0,2))
        self.label_size.grid(row=2, column=0, pady=(0,2))
        self.combobox_size.grid(row=2, column=1, pady=(0,2))
        self.label_neighborhood.grid(row=2, column=2, pady=(0,2))
        self.combobox_neighborhood.grid(row=2, column=3, padx=(0,10), pady=(0,2))

class Additionals:

    def __init__(self, master: Tk) -> None:
        """Create additionals listbox frame

        Args:
            master (Tk): Root window
        """
        self.root = master
        self.additionals_type = ['cereais', 'chocolates', 'coberturas', 'derivados do leite', 'diversos', 'frutas']

        for i in range(0,len(self.additionals_type)):
            cur_type =self.additionals_type[i]
            self.list_itens = self.mong.read_item(cur_type, 'adicionais')
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
            globals()[f'frame_{cur_type}'] = ttk.Frame(self.root)
            globals()[f'scrollbar_{cur_type}'] = Scrollbar(globals()[f'frame_{cur_type}'],
                orient=VERTICAL
                )
            globals()[f'listbox_{cur_type}'] = Listbox(globals()[f'frame_{cur_type}'], 
                font=('Apple LiGothic', 10),
                selectmode=MULTIPLE, 
                exportselection=False,
                yscrollcommand=globals()[f'scrollbar_{cur_type}'].set
            )
            for j in range(0, len(self.list_itens)):
                globals()[f'listbox_{cur_type}'].insert(END, self.list_itens[j])

            globals()[f'label_{cur_type}'] = ttk.Label(globals()[f'frame_{cur_type}'], 
                text=cur_type.upper()
            ).grid(row=0, column=0)

            globals()[f'frame_{cur_type}'].grid(row=start_row, column=k, rowspan=8, padx=p, pady=(0,20))
            globals()[f'listbox_{cur_type}'].grid(row=1, column=0)
            globals()[f'scrollbar_{cur_type}'].grid(row=1, rowspan=8, column=1, sticky=NS)
            globals()[f'scrollbar_{cur_type}'].config(command=globals()[f'listbox_{cur_type}'].yview)
    
    
class ButtonAndObs(Header, Additionals):

    
    def __init__(self, master: Tk, id_user) -> None:
        """Create buttons and textbox frame

        Args:
            master (Tk): Root window
            id_user (int): ID user to save sheet i your name.
        """
        Header.__init__(self, master)
        Additionals.__init__(self, master)
        self.command = tkf.CommandButtons(window=self.root, id_user=id_user)
        
        self.frame_buttons = ttk.Frame(self.root)
        self.button_ok = Button(self.frame_buttons, 
                                text='SALVAR', 
                                width=15, 
                                height=2,
                                background='lime',
                                command=lambda: self.command.send_data(self.entry_sheet_number, 
                                                                       self.combobox_combo_name, 
                                                                       self.combobox_payment_option, 
                                                                       self.entry_price, 
                                                                       self.combobox_size, 
                                                                       self.combobox_neighborhood, 
                                                                       self.textbox_obs,
                                                                       self.json_listbox()),
                                cursor='hand2'
                                )
        self.button_close = Button(self.frame_buttons, 
                                   text='VOLTAR AO PERFIL', 
                                   width=15, 
                                   height=2, 
                                   background='red',
                                   command=lambda: self.command.close_window(),
                                   cursor='hand2'
                                   )
        self.button_clear = Button(self.frame_buttons,
                                   text='Limpar', 
                                   width=15, 
                                   height=2, 
                                   background='yellow',
                                   command=lambda: self.command.clear_widgets(),
                                   cursor='hand2'
                                   )
        self.label_obs = LabelFrame(self.frame_buttons, 
                                    text='Observações', 
                                    bg=PRIMARY_BG_COLOR,
                                    foreground=DEFAULT_FG_COLOR, 
                                    font=('Apple LiGothic', 15)
                                    )
        self.textbox_obs = Text(self.label_obs, 
                                width=52, 
                                height=5,
                                font=('Apple LiGothic', 10)
                                )
        self.frame_buttons.grid(row=16, column=2, columnspan=2, padx=(20,20))
        self.button_ok.grid(row=1, column=0, pady=(0,20))
        self.button_clear.grid(row=1, column=1, padx=(10,10), pady=(0,20))
        self.button_close.grid(row=1, column=2, padx=(0, 10), pady=(0,20))
        self.label_obs.grid(row=0, column=0, columnspan=3, padx=(0, 10), pady=(0,20))
        self.textbox_obs.grid(row=0, column=0, rowspan=11)
        
    def json_listbox(self):
        json_datas = {}
        for i in self.additionals_type:
            json_datas[i] = self.__create_dict_additionals(globals()[f'listbox_{i}'])
        print(json_datas)
        return json_datas
    
    def __create_dict_additionals(self, listbox_name: Listbox) -> list:
        list_temp = [listbox_name.get(i) for i in listbox_name.curselection()]
        return list_temp