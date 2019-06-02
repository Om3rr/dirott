import requests
import os
USERNAME = "Omertesttbot"
CHAT_ID = "@iloveaya"
API_KEY = os.environ.get("TELEGRAM_API_KEY")

def send_dira(dira):
    for image in dira.images():
        if not image:
            continue
        requests.post("https://api.telegram.org/bot{API_KEY}/sendPhoto".format(API_KEY=API_KEY),
        data={
            "chat_id": CHAT_ID,
            "photo": image,
        })
    req = requests.post(
        "https://api.telegram.org/bot{API_KEY}/sendMessage".format(API_KEY=API_KEY),
        data={
            "chat_id": CHAT_ID,
            "text": dira.to_telegram(),
            "parse_mode": "Markdown"
        }
    )
