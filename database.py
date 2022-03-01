import array

import pymongo


class Database:
    def __init__(self, database: str, collection: str):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.collection = client[database][collection]

    def insert(self, data: object):
        print(self.collection.insert_one(data))

    def insert_one(self, data: object):
        print(self.collection.insert_one(data))

    def find(self, data: object):
        return self.collection.find(data)

    def find_one(self, data: object):
        return self.collection.find_one(data)

    def find_random(self):
        word = self.collection.aggregate([{'$sample': {'size': 1}}])
        return list(word)[0]

    def add_words(self, words: array):
        for word in words:
            self.collection.insert_one({
                'word': word,
                'difficulty': 1 if len(word) < 5 else 2 if len(word) < 8 else 3
            })

    def update(self, where: object, update: object):
        self.collection.update_one(where, update)

    def delete(self, game_code):
        self.collection.delete_one({'gameCode': game_code})
