from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/')
def index():
    return "<img src=https://i.imgur.com/6ccwLT4.gif>"
            

def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()
    