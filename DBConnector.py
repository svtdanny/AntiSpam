import pymongo

class DBConnector():
    def __init__(self, address, port, db_name):
        client = pymongo.MongoClient('localhost', 27017)
        self.connection = client[db_name]

    def find_document(self, collection, elements, multiple=False):
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements.
        """
        if multiple:
            results = self.connection[collection].find(elements)
            return [r for r in results]
        else:
            return self.connection[collection].find_one(elements)

    def insert_document(self, collection, data, multiple=False):
        """ Function to insert a document into a collection and
        return the document's id.
        """
        if multiple:
            return self.connection[collection].insert_many(data).inserted_id
        else:
            return self.connection[collection].insert_one(data).inserted_id

    def update_document(self, collection, query_elements, new_values, multiple=False):
        """ Function to update a single document in a collection.
        """
        if multiple:
            return self.connection[collection].update_many(query_elements, {'$set': new_values},  True)
        else:
            return self.connection[collection].update_one(query_elements, {'$set': new_values},  True)

    def delete_document(self, collection, query, multiple=False):
        """ Function to delete a single document from a collection.
        """
        if multiple:
            return self.connection[collection].delete_many(query)
        else:
            return self.connection[collection].delete_one(query)

    def write_from_df(self, collection, df, method = 'replace'):
        """
        method - 'replace'/'insert'
        """
        if method == 'replace':
            self.delete_document(collection, {}, multiple=True)
        for row in df.values:
            doc = dict(zip(df.columns, row))
            self.insert_document(collection, doc)

    def get_settings(self, login):
        return self.find_document('Settings', {'login':login})
    
    def set_settings(self, login, settings):
        return self.update_document('Settings', {'login':login}, settings)
    
    def read_as_df(self, collection):
        res = self.find_document(collection, {}, multiple=True)
        res = pd.DataFrame(res)
        if len(res) != 0:
            res.drop(['_id'], axis=1, inplace=True)
        else:
            print('data is empty!')
        return res

db = DBConnector('localhost', 27017, 'BaseDB')

## Check settings working peoperly:
res = db.set_settings('root', {'login':'root', 'volume':2, 'set1':'enable'})
print(res)

res = db.get_settings('root')
print(res)

res = db.set_settings('root', {'login':'root', 'volume':22, 'set1':'disable'})
print(res)

res = db.get_settings('root')
print(res)

#check write from df works fine
import pandas as pd
df = pd.read_csv('./breast-cancer.csv')
print(df)

db.write_from_df('TestDataset', df)
#res = db.find_document('TestDataset', {}, True)
res = db.read_as_df('TestDataset')
print(res)

#Delete testing data
res = db.delete_document('Settings', {'login':'root'}, multiple=True)
print(res)
res = db.delete_document('TestDataset', {}, multiple=True)
print(res)

#Check if deleted and undefined behavior with 
res = db.get_settings('root')
print(res)
res = db.read_as_df('TestDataset')
print(res)