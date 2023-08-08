import json
import requests
from urllib.parse import urlparse
from time import sleep 
from flask import Flask, request
import asyncio
from characterai import PyAsyncCAI

app = Flask(__name__)

async def asyncHela(message):
    client_hela = PyAsyncCAI('aciHa-7oXJih543TrBrR-O_PiZN-8lrdb9s4Bb6_73Q')
    await client_hela.start()
    print("message", message)
    data = await client.chat.send_message('CHAR', message)
    m = data['replies'][0]['text']
    print("message", m)
    return m

@app.route("/")
def index():
    return "OK"

@app.route("/Hela")
def hela():
    message = request.args.get('message')
    
    return asyncHela(message)
    
if __name__ == "__main__":
    asyncio.run(asyncHela())
    app.run(host='0.0.0.0', port=3000, debug=True)
