
from flask import Flask
from pymongo import MongoClient
import threading

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client["mongo-test"]
collection = db["mongo-coll"]

# Create a lock
lock = threading.Lock()

# Counter variable
# counter = 0

@app.route('/increment', methods=['POST'])
def increment_counter():
    # global counter

    try:
        # Acquire the lock
        lock.acquire()

        # Increment the counter
        

        # Update the counter value in MongoDB
        # ab =collection.find_one_and_update({}, {"$inc": {"counter": 1}}, upsert=True)
        doc = collection.find_one_and_update({}, {"$inc": {"counter": 1}})
        new_counter_value = doc["counter"] + 1

        return {"value": new_counter_value}
    finally:
        # Release the lock
        lock.release()


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True,port=4000)
