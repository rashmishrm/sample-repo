from flask import Flask
from flask import request
from flask import json


app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!! changed file ddddd"



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)

    
