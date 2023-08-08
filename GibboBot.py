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
    
    data = await client.chat.send_message('CHAR', message)
    print("response: ", data)
    
    return jsonify(data), 200

@app.route("/")
def index():
    return "OK"

@app.route("/Hela")
def hela():
    message = request.args.get('message')
    return asyncHela(message)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
