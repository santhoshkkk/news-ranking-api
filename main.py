from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/rank', methods=['GET'])
def call_function():
    return "5";


app.run(host="0.0.0.0")


