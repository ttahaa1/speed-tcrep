import time
from pyrogram import Client, errors

api_id = '22379637'
api_hash = '7a5777d4bd0480856f9e7b129acc7a9f'
session_string = 'BAFEO3QAgkEJI1MmV8sUSTdWXsAgpeJbXTHCPHFaonehGZd8flub_RgYgX8rOBTDKMYcp_NxyAHUzcxXx5Tm_9151SkT8ntmlodNYSmGPvYQJizS0zbuHU6nZCjhKwWbfdBbEP9ez6x94nmf_lb6bWygn4J5Jv5A8709NUtmKpldhhg3P8Z0TSHYr2q3N9GvDriaoylnKOX-4Y8LiMpIolAJxI1TkB2JXDz8UhrIW_L-vQ51uh2oJB3x3EUDvY3nkF4Zg8NXhwlNYEzlSOpbe_JK4IefHZJUu-3_KFO7SNWAxlZLYTx_rR3VNDK1QR30J_VKpyJdLTf8_gQgTdb3PCYCzxBcoAAAAAGJ8ONCAA'

start_number = 16
end_number = 28  

links = [f"https://t.me/c/2027544784/{i}" for i in range(start_number, end_number + 1)]

app = Client("my_account", api_id=api_id, api_hash=api_hash, session_string=session_string)

app.start()

for link in links:
    print("Sending link:", link)
    retries = 3
    for attempt in range(retries):
        try:
            app.send_message('@save_speed_bot', link)
            print(f"Link {link} sent successfully.")
            time.sleep(30)
            break
        except errors.FloodWait as e:
            print(f"FloodWait error: Waiting for {e.x} seconds.")
            time.sleep(e.x)
        except errors.RPCError as e:
            print(f"RPCError: {e}. Retrying...")
            time.sleep(5)
        except Exception as e:
            print(f"Unexpected error: {e}. Retrying...")
            time.sleep(1)
    else:
        print(f"Failed to send link {link} after {retries} attempts.")

app.stop()
