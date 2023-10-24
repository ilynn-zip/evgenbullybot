from flask import Flask, request
from threading import Thread
from waitress import serve
import time
import requests
 
 
app = Flask('')
 
@app.route('/')
def home():
  return "I'm alive"
 
def run():
  serve(app, host="0.0.0.0", port=8080)
  #app.run(host='0.0.0.0', port=80)
 
def keep_alive():
  t = Thread(target=run)
  t.start()
