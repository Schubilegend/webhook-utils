import requests
import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=False)


print(Fore.GREEN + """
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ██╗   ██╗████████╗██╗██╗     ███████╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██║   ██║╚══██╔══╝██║██║     ██╔════╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ██║   ██║   ██║   ██║██║     ███████╗
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ██║   ██║   ██║   ██║██║     ╚════██║
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ╚██████╔╝   ██║   ██║███████╗███████║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝
by Schubilegend                                                                                                     
""")
print("Welcome To Webhook Utils!")
print("1. Spam Webhook")
print("2. Delete Webhook")
print("3. Webhook info")
selection = input("Please select an option: ")

if selection == "1":
    webhook = input("Enter webhook URL: ")
    username = input("Enter name to spam as(can be left empty): ")
    if username == "":
        username = "Spammed with Webhook Utils by Schubilegend"
    message = input("Enter message to spam: ")
    amount = int(input("Enter amount of messages to spam: "))
    delay = int(input("Enter delay in seconds: "))
    tts = input("Enable TTS? (y/n): ")
    if tts == "y":
        tts = True
    else:
        tts = False
    data = {
        "content": message,
        "username": username,
        "tts": tts
    }
    webhook_test = requests.get(webhook)
    if webhook_test.status_code == 200:
        print("Webhook valid! Starting spam...")
        while amount != 0:
            r = requests.post(webhook, data=data)
            amount -= 1
            print("Message sent! " + str(amount) + " Messages left!")
            time.sleep(delay)
            if amount == 0:
                print("Done!")

    else:
        print("Invalid webhook!")
elif selection == "2":
    webhook = input("Enter webhook URL: ")
    validate_webhook = requests.get(webhook)
    if validate_webhook.status_code == 200:
        print("Webhook valid! Deleting webhook...")
        r = requests.delete(webhook)
        if r.status_code == 204:
            print("Webhook deleted!")
        else:
            print("Error deleting webhook!")
    else:
        print("Invalid webhook!")
elif selection == "3": 
    webhook = input("Enter webhook URL: ")
    try:

        response = requests.get(f"{webhook}")
        if response.status_code == 200:
            print("Webhook valid! Getting info...")
            data = response.json()
            Name = str(data["name"])
            ChannelID = str(data["channel_id"])
            GuildID = str(data["guild_id"])
            Token = str(data["token"])
            Avatar = str(data["avatar"])
            ID= str(data["id"])
            print(f"Name: {Name}")
            print(f"Channel ID: {ChannelID}")
            print(f"Guild ID: {GuildID}")
            print(f"Token: {Token} (Skids, This is useless)")
            print(f"Avatar: {Avatar}")
            print(f"ID: {ID}")
        else:
            print("Webhook doesnt exists anymore!")
    except:
        print("Error getting webhook info!")
else:
    print("Invalid option!")
