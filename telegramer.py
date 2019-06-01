import requests
USERNAME = "Omertesttbot"
CHAT_ID = "@iloveaya"
API_KEY = "SECRET"

def send_dira(dira):
    req = requests.post(
        "https://api.telegram.org/bot{API_KEY}/sendMessage".format(API_KEY=API_KEY),
        data={
            "chat_id": CHAT_ID,
            "text": dira.to_telegram(),
            "parse_mode": "Markdown"
        }
    )
    print(req.content)