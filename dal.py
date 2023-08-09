from pymongo import MongoClient

class PostDAL:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['mydatabase']
        self.collection = self.db['posts']

    def get_all_posts(self):
        return self.collection.find()

    def get_post_by_id(self, post_id):
        return self.collection.find_one({'_id': post_id})

    def create_post(self, post_data):
        return self.collection.insert_one(post_data)

    def update_post(self, post_id, post_data):
        return self.collection.update_one({'_id': post_id}, {'$set': post_data})

    def delete_post(self, post_id):
        return self.collection.delete_one({'_id': post_id})