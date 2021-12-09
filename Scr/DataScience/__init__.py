import json
from pymongo import MongoClient
import mysql.connector
import pandas as pd
import numpy as np

COLUMNS_NAME = ['Nº da Comanda',  'Vendedor', 'Combo', 'F. de Pagamento', 'Preço', 'Tamanho', 'Bairro', 'Cereais', 'Chocolates', 'Coberturas', 'Derivados do Leite', 'Diversos', 'Frutas', 'Obs', 'Data']

SELLER = ('seller', 'Vendedor')
COMBO = ('combo', 'Combo')
PAYMENT_TYPE = ('payment_type', 'F. de Pagamento')
PRICE = ('price', 'Preço')
SIZE = ('size', 'Tamanho')
NEIGHBORHOOD = ('neighborhood', 'Bairro')

class ManipulationDB:
    def __init__(self) -> None:
        """Create connection in databases
        """
        #Connect MongoDB
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['acaiteria']

        #Connect MySQL
        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='', database='acaiteria')
    
    def create_dataframe(self, with_seller_name=False) -> pd.DataFrame:
        """Create data frame with data of sells

        Args:
            with_seller_name (bool, optional): [description]. Defaults to False.

        Returns:
            pd.DataFrame: [description]
        """
        i = dict()
        collection = self.db['comandas']
        cursor = collection.find({})

        df_main = pd.DataFrame(self.__pretty_json(cursor[0], with_seller_name), columns=COLUMNS_NAME)

        for i in cursor[1::]:
            df_temp = pd.DataFrame(self.__pretty_json(i, with_seller_name), columns=COLUMNS_NAME)
            df_main = pd.concat([df_main, df_temp])
        
        cursor.close()
        return df_main

    def __pretty_json(self, sheet: str, with_name=False) -> dict:
        """Create a pretty json format

        Args:
            sheet (str): dict of a record
            with_name (bool, optional): If True seller column will be seller name else will be ID seller. Defaults to False.

        Returns:
            dict: Dict containing record data 
        """
        old_json = sheet
        pretty_sheet = dict()
        pretty_sheet['number_sheet'] = old_json['n_comanda']
        pretty_sheet['seller'] = self.__name_seller(old_json['seller']) if with_name else old_json['seller']
        pretty_sheet['combo'] = old_json['combo']
        pretty_sheet['payment_type'] = old_json['f_pagamento']
        pretty_sheet['price'] = old_json['preco']
        pretty_sheet['size'] = old_json['tamanho']
        pretty_sheet['neighborhood'] = old_json['bairro']
        pretty_sheet['cereals'] = list(i for i in old_json['cereais'])
        pretty_sheet['chocolates'] = list(i for i in old_json['chocolates'])
        pretty_sheet['covers'] = list(i for i in old_json['coberturas'])
        pretty_sheet['milk_derivatives'] = list(i for i in old_json['derivados do leite'])
        pretty_sheet['several'] = list(i for i in old_json['diversos'])
        pretty_sheet['fruits'] = list(i for i in old_json['frutas'])
        pretty_sheet['obs'] = old_json['obs']
        pretty_sheet['date'] = old_json['date_time']

        json_pretty = json.dumps(pretty_sheet, indent=4, ensure_ascii=False).encode('utf8')
        json_pretty = [json.loads(json_pretty.decode()).values()]
        return json_pretty
    
    def export_excel(self, dataframe: pd.DataFrame, path: str) -> None:
        """Export data frame to excel file

        Args:
            dataframe (pd.DataFrame): Data frame to convert excel file
            path (str): File path
        """
        dataframe.to_excel(path, 'Todas as Comandas', encoding='utf-8')
    
    def statistical_equations(self) -> tuple:
        """Calculate statistical metrics

        Returns:
            tuple: Contaning claculations results
        """
        df = self.create_dataframe()
        
        sales_quantity = df['Nº da Comanda'].count()
        revenue = df['Preço'].sum()
        mean_sales = round(df['Preço'].mean(), 2)

        return (sales_quantity, revenue, mean_sales)
    
    def quantity_type(self, names: tuple)-> pd.DataFrame:
        """Create data frame groupy by any colum type

        Args:
            names (tuple): Value used to group the column. Suppot values: SELLER, COMBO, PAYMENT_TYPE, PRICE, SIZE, NEIGHBORHOOD

        Returns:
            pd.DataFrame: Data frame group by column 
        """
        df = self.create_dataframe()

        quantitys = dict()
        if names != SELLER:
            cursor = self.db['dadosGerais'].find({'_id': names[0]})
            types_names = list(i for i in cursor[0].keys() if i != '_id')
        else:
            cursor = self.conn.cursor()
            cursor.execute('SELECT primeiro_nome, sobrenome FROM empregados')
            types_names = list(map(lambda x: f'{x[0]} {x[1]}', cursor))
        if names == SIZE:
            types_names = list(map(self.__str_numeric, types_names))
        for i in types_names:
            qtd = 0
            for j in df[names[1]]:
                if j == i:
                    qtd += 1
            quantitys[i] = qtd 
        quantity_any_thing = pd.DataFrame.from_dict(quantitys, orient='index', columns=['Qtd.'])
        
        cursor.close()
        return quantity_any_thing
    
    def __str_numeric(self, str: str) -> int:
        """Return only number of a str

        Args:
            str (str): String to convert

        Returns:
            int: Only numbers os string
        """
        only_number = ''
        for i in str:
            if i.isnumeric():
                only_number += i
        if only_number == '1':
            only_number = '1000'
        return int(only_number)
    
    def __name_seller(self, id: int) -> str:
        """Return name of seller according to ID

        Args:
            id (int): ID seller

        Returns:
            str: NAme seller
        """
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT primeiro_nome, sobrenome FROM empregados WHERE id = {id}')
        employee_name = list(map(lambda x: f'{x[0]} {x[1]}', cursor))

        cursor.close()
        return employee_name[0]

dataScience = ManipulationDB()

#dataScience.export_excel(dataScience.create_dataframe(), 'C:/Users/USER/OneDrive/Documentos/Programação/Python/Projetos/Comandas-Açai/Scr/SupportFiles/comandas.xlsx')

print(dataScience.quantity_type(SELLER))