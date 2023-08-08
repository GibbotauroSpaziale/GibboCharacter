import json
import requests
from urllib.parse import urlparse
from time import sleep 
from flask import Flask, request
import asyncio
from characterai import PyAsyncCAI

app = Flask(__name__)

client_hela = PyAsyncCAI('aciHa-7oXJih543TrBrR-O_PiZN-8lrdb9s4Bb6_73Q')

@app.route("/")
def index():
    return "OK"

@app.route("/Hela")
def hela():
    client_hela.start()
    message = request.args.get('message')
    print("message: ",message);
    
    data = client_hela.chat.send_message('CHAR', message)
    print("data: ",data);
    ms = data['replies'][0]['text']
    
    response = requests.post(url, json={"rply": ms})
    return ms


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
