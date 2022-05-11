import pymongo
from pymongo import MongoClient
from datetime import datetime
class MongoFunctions:

    def __init__(self) -> None:
        """Connect to MongoDB
        """
        #Connect database
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['acaiteria']

    def __last_id_recorded(self) -> int:
        """Query the last id

        Returns:
            int: ID number
        """
        cursor = self.db['comandas'].find({}).limit(1).sort("$natural", pymongo.DESCENDING)
        for i in cursor:
            last_record = i
        try:
            return last_record['_id']
        except:
            return 0

    def insert_item(self, document: dict) -> None:
        """Inser one document in collection

        Args:
            document (dict): Dict containing the data
        """
        #Insert item in collection
        collection = self.db['comandas']
        document['_id'] = (self.__last_id_recorded() + 1)
        document['date_time'] = str(datetime.today())
        collection.insert_one(document)
    
    def read_item(self, _id: str, collection: str) -> list:
        """Collect data of collection

        Args:
            _id (str): ID of record
            collection (str): Name collection

        Returns:
            list: List containing the past _id record 
        """
        col = self.db[collection]
        cursor = col.find({"_id": _id})
        list_combos = []
        for k in cursor[0].keys():
            list_combos.append(k)
        list_combos.remove('_id')
        return list_combos


    
