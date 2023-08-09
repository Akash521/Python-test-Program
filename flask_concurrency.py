from flask import Flask
from threading import Lock

app = Flask(__name__)
lock = Lock()
value = 0

@app.route('/increment', methods=['GET'])
def increment_value():
    global value
    value += 1
    # with lock:
    #     value += 1
    return {"Value": value}

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True,port=4000)