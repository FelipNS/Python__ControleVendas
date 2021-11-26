import pymongo
from pymongo import MongoClient
from datetime import datetime
class MongoCRUD:

    def __init__(self) -> None:
        #Connect database
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['acaiteria']
        self.collection = self.db['comandas']

    def _last_id_registered(self) -> int:
        cursor = self.collection.find({}).limit(1).sort("$natural", pymongo.DESCENDING)
        for i in cursor:
            last_register = i
        try:
            return last_register['_id']
        except:
            return 0

    def insert_item(self, document: dict) -> None:
        #Insert item in collection
        document['_id'] = (self._last_id_registered() + 1)
        document['date_time'] = str(datetime.today())
        self.collection.insert_one(document)

    def _format_date(self, date: str) -> str:
        splited_date = date.split('-')
        day_and_time = splited_date[2]
        splited_date.pop(-1)
        day_and_time = day_and_time.split(' ')
        return f'{day_and_time[0]}/{splited_date[1]}/{splited_date[0]} {day_and_time[1][:8]}'

    def _print_sheet(self, filtered_list: list) -> None:
        for i in filtered_list:
            for k, v in i.items():
                if k == '_id':
                    k = f"Número da comanda: {v}"
                elif k == 'date_time':
                    k = f'Data: {self._format_date(v)}'
                print(f'{k}')

    def read_item(self, date = '') -> None:
        cursor = self.collection.find({'date_time': {'$gte': date}})
        registered = []
        for i in cursor:
            registered.append(i)
        self._print_sheet(registered)
    
    def update_item(self, filter: dict, new: dict) -> None:
        self.collection.update_one(filter, {"$set": new})

    def delete_item(self, filter: dict) -> None:
        self.collection.delete_one(filter)

class MongoReadCollection:

    def __init__(self, collection_name: str) -> None:
        #Connect database
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['acaiteria']
        self.collection = self.db[collection_name]

    def read_item(self, _id: str) -> list:
        cursor = self.collection.find({"_id": _id})
        list_combos = []
        for k in cursor[0].keys():
            list_combos.append(k)
        list_combos.remove('_id')
        return list_combos

    
