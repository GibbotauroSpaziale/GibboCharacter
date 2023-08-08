import json
import requests
from urllib.parse import urlparse
from time import sleep 
from flask import Flask, request
import asyncio
from characterai import PyAsyncCAI, PyCAI

app = Flask(__name__)
"""
async def asyncHela(message):
    client_hela = PyAsyncCAI('aciHa-7oXJih543TrBrR-O_PiZN-8lrdb9s4Bb6_73Q')
    print("client_hela init")
    await client_hela.start()
    print("client_hela started")
    data = await client.chat.send_message('CHAR', message)
    m = data['replies'][0]['text']
    print("message", m)
    return m
"""
@app.route("/")
def index():
    return "OK"

@app.route("/Hela")
def hela():
    message = request.args.get('message')

    client = PyCAI('aciHa-7oXJih543TrBrR-O_PiZN-8lrdb9s4Bb6_73Q')
    data = client.chat.send_message('CHAR', message)
    
    ms = data['replies'][0]['text']
    print(f"name: {message}")
    return "ok" #asyncHela(message)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
