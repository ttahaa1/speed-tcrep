import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = '22379637'
api_hash = '7a5777d4bd0480856f9e7b129acc7a9f'
session_string = 'BAFZ12oALm94m_eFubUPqFu0ndf9cqR9zVMThREtlfUZJ6w418Kvm75Jj5KBUPk4Vz5Q1KEpHrfqcYjEuQAp13wrAV1iiOq352VS0goJ1h9-f3FcFC2bGcgSB3Z2jt_JvIaEENFDW9n02NbbNwWXJ4kxvqzgAyoeMlRNaitHIowedlo4z4eTmptAVK3ud_eIHDTNiPkmBLEwCSfeQXpBtM5ZVVM-jGGuyo64gM_XYqhJbVc2IZc6UPkV7w6uG4BfWaDJydyIU32Vm52HBgkJI-WDWRihTjLnfjNUmNFoxfi3qDxYEUKrms2zphv2lZhNvzl4o9ulaUZeDWmFImArZb-8WCG_zAAAAAFUEtNnAA'

start_number = 2
end_number = 186

links = []
for i in range(start_number, end_number + 1):
    link = f"https://t.me/c/2056146498/{i}"
    links.append(link)

with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
    for link in links:
        print("Sending link:", link)
        client.send_message('@save_speed_bot', link)
        time.sleep(80)
