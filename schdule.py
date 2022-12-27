import time
import atexit
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'


@app.route("/statuscodechecker", methods=["GET", "POST"])
def statuschecker():
    requests.get("https://www.google.com/")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))  # time.strftime convert a time string to tuple
    return "Welcome Home :) !"

@app.route("/sslcheck", methods=["GET", "POST"])
def sslcheck():
    requests.get("https://www.google.com/")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))  # time.strftime convert a time string to tuple
    return "Welcome Home :) !"



scheduler = BackgroundScheduler()
scheduler.add_job(func=statuschecker, trigger="interval", minutes=13)  # seconds=60)
scheduler.add_job(func=sslcheck, trigger="interval", minutes=17)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

app.run(host='0.0.0.0', port=81)