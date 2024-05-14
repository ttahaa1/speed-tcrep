import time
from telethon.sync import TelegramClient

api_id = '22379637'
api_hash = '7a5777d4bd0480856f9e7b129acc7a9f'
session_name = 'SESSIONNAME'

start_number = 2
end_number = 186

links = []
for i in range(start_number, end_number + 1):
    link = f"https://t.me/c/2056146498/{i}"
    links.append(link)

with TelegramClient(session_name, api_id, api_hash) as client:
    for link in links:
        print("Sending link:", link)
        print("#(???? ??? ???????)mahmoud ??")
        client.send_message('@save_speed_bot', link)
        time.sleep(80)
