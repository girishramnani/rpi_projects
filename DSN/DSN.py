from flask import Flask,request, session, g, redirect, url_for
from model import Database
import os
from config import CONFIG


app = Flask(__name__)
app.config.from_object(CONFIG)



x = Database(app)
x.init_db()



@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/api",methods=["POST","GET"])
def api():
    pass



if __name__ == '__main__':
    app.run()
