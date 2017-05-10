from flask import Flask
from flask import request
from flask import json


app = Flask(__name__)
@app.route("/")
def hello():
    return "changed from Dockerized Flask App!! changed file ddddd HHHHHHHHHH"







if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)

    
