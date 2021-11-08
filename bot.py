import time
from telethon.sync import TelegramClient
from telethon import errors
from telethon.tl.custom.message import Message
from telethon.tl.custom.chatgetter import ChatGetter
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import sys
import json
import csv

api_id = "api_id"
api_hash = 'api_hash_code'
phone = 'phone_number'
client = TelegramClient(phone, api_id, api_hash)

SLEEP_TIME = 30

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))    

input_file = sys.argv[1]
users = []
me = client.get_entity("userid")

with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = me.username
        user['id'] = me.id
        user['access_hash'] = me.access_hash
        user['name'] = me.first_name
        users.append(user)

for name in client.get_dialogs(1):
    group_name = name.name

i = True
while i == True:
    try:
        for message in client.iter_messages(group_name, limit=1):
            print(message.sender_id, ':', message.text)
            rec_msg = message.text
            rec_id = message.sender_id
            for message in client.iter_messages("karamazovic", limit=1):
                last_msg = message.text
                print(last_msg)
                if rec_msg != last_msg:
                    client.send_message("karamazovic", rec_msg)
                else:
                    time.sleep(5)
    except:
        pass

client.disconnect()
