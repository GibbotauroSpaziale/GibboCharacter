import json
import requests
from time import sleep 
from flask import Flask, request
import asyncio
from characterai import PyAsyncCAI

app = Flask(__name__)

client_hela = PyAsyncCAI('TOKEN')

async def a_hela(m):
    await client_hela.start()
    return await client_hela.chat.send_message('CHAR', m)

@app.route("/")
def index():
    return ""

@app.route("/Hela")
def hela():
    message = request.args.get('message')

    data = a_hela(message)
    message = data['replies'][0]['text']
    name = data['src_char']['participant']['name']
    
    url = "https://api.mixitupapp.com/api/webhook/901c6ed5-ccf4-46cf-c5fe-08db11eb059d?secret=AEECC476EE3789E59BED5404E78210A8CE4474FFE8E9AB6D398C64E01E31F4D2"
    rp = {"rply": message}
    response = requests.post(url, json=rp)
    return message


if __name__ == "__main__":
    app.run(host='0.0.0.0', rocess.env.PORT || 3000, debug=True)
