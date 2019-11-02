import os
import json
from urllib.request import urlopen
import time
from urllib.parse import quote,unquote
import requests
from telebot import telegram
from time import sleep

# Set your token Here . in the first you must have telegram bot and config it by BotFother
token='xxxxxxxxxxxxxxxxxxxxxxxxxxx'
command='getme'
url='https://api.telegram.org/bot{}/'.format(token)
onlyurl='https://api.telegram.org/bot'

proxy=""
connection={
    "url":onlyurl,
    "token":token,
    "command":command,
    "proxy":proxy,
}
tlg=telegram(connection)


while True:
    time.sleep(1)
    req=tlg.getupdates()
    print("new request ...  "+str(req))
    if req:
        print(str(req))
        if req["text"]=="xxxxxx" or req["text"]=="xxxxxxxx":
            data="your answer - text for req"
            if tlg.sendmessage(req["chat_id"],quote(str(data)),req["upid"]):
                tlg.getupdates(req["upid"])                
        elif req["text"]=="help" or req["text"]=="Help":
            data="help text"
            if tlg.sendmessage(req["chat_id"],quote(str(data)),req["upid"]):
                tlg.getupdates(req["upid"])                
            else:
                tlg.getupdates(req["upid"])