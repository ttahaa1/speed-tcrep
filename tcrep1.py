import time
from pyrogram import Client

api_id = '22379637'
api_hash = '7a5777d4bd0480856f9e7b129acc7a9f'
session_string = 'BAFVfHUAoB_2VLY242pL_NfC5WZZP-xk0CB_8ddWdbQbIdGANJbd2QWU0y_A97m1NelotzdKoRMo6lZKtOysW9cX0WNDS47_s024HnqgXYqjtlJ737TGfRPyZAZPwslMTJMwz8caJ5xfAJD8-FzWyxIK5Nrx7xJBk3PulAdyxxKskn2cC1zB7ZbByqEUiEmyvbOwUtqV4CM8YzSlwMC1k2VYEiuelyeUoaOEAXH2PG1OVtaFGRdtvWx6yI-gcW1pIT9KX8OrTn7Ic8Vw7L1P7dPfq9VzqcvPKskmUF6wx5YgKmFuQtF4L7henBXxkF02LygO-U7oM0zb0F8hX5phUc1FQyhkqAAAAAFcHHoOAA'

start_number = 2
end_number = 186

links = [f"https://t.me/c/2056146498/{i}" for i in range(start_number, end_number + 1)]

app = Client("my_account", api_id=api_id, api_hash=api_hash, session_string=session_string)

app.start()

for link in links:
    print("Sending link:", link)
    app.send_message('@save_speed_bot', link)
    time.sleep(80)

app.stop()
