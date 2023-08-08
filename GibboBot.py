import json
import requests
from urllib.parse import urlparse
from time import sleep 
from flask import Flask, request
import asyncio
from characterai import PyAsyncCAI

app = Flask(__name__)

client_hela = PyAsyncCAI('aciHa-7oXJih543TrBrR-O_PiZN-8lrdb9s4Bb6_73Q')

async def a_hela(m):
    await client_hela.start()
    return await client_hela.chat.send_message('CHAR', m)

@app.route("/")
def index():
    return "OK"

@app.route("/Hela")
def hela():
    parsed = urlparse.urlparse(request)
    message = urlparse.parse_qs(parsed.query)['some_key'][0]
    print(message);
    
    data = a_hela(message)
    ms = data['replies'][0]['text']
    name = data['src_char']['participant']['name']

    rp = {"rply": ms}
    response = requests.post(url, json=rp)
    return ms


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
