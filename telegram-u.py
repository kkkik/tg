import telethon
import time#Im Aymen 🐊
from telethon import events
from telethon.sync import functions
from telethon import TelegramClient
from telethon.tl.functions.messages import GetPeerDialogsRequest
client = TelegramClient("Client", 25635928, '6e49a338bcf4c3406afdb0ce9a2892e1')
t = time.strftime("%M:%S")
client.start()
client.send_message("me", "Ok , Send me user like /pin user ")
@client.on(events.NewMessage(outgoing=True, pattern=r"/pin"))
async def save(event):
    clicks = 1;msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1);username = str(msg[0]);await event.reply(f"Now , go delete channel for all users @{username}")
    try:
     while True:clicks += 1;print(f"- UserName [ @{username} ] [{clicks}].");await client(GetPeerDialogsRequest(peers=[username]))
    except ValueError:await client.send_message("me","We Waiting ?")
    except telethon.errors.rpcerrorlist.UsernameNotOccupiedError:
        try:await client(functions.account.UpdateUsernameRequest(username=username));print("\d - UserName [ @{username} ] ."+clicks)
        except Exception as error:
            if "wait" in str(error):await client.send_message(event.chat.id, f"Flood - {error.seconds} ️.");print("\d - UserName [ @{username} ] ."+clicks);pass
            else:await client.send_message(event.chat_id, f'Error Message : {error}\nUserName : {username}');print("\d - UserName [ @{username} ] ."+clicks)
        else:await client.send_message("me", f'Ok , Catched to the account');print("\d - UserName [ @{username} ] ."+clicks)
    except telethon.errors.rpcerrorlist.ChannelPrivateError:await client(functions.account.UpdateUsernameRequest(username=username));await client.send_message("me", f'• UserName : @{username} .\n• Clicks : {clicks}\n• In Your Account\n• Time : {t}/n• Dev : @K_n_Y')
client.run_until_disconnected()