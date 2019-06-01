import requests
from dira import Dira

class Scraper:
    def __init__(self):
        self.session = requests.session()
        self.session.headers = {
            "X-MOD-SBB-CTYPE": "xhr",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }


    def get_dirot(self, hood=573, price_low=3000, price_high=4500):
        print("hood", hood, "low", price_low, "high", price_high)
        url = "https://www.yad2.co.il/api/pre-load/getFeedIndex/realestate/rent?city=3000&neighborhood={hood}&price={low}-{high}&compact-req=1".format(
            hood=hood, low=price_low, high=price_high
        )
        resp = self.session.get(url).json()
        dirots = []
        for item in resp["feed"]["feed_items"]:
            if not Dira.relevant(item):
                continue
            dirots.append(Dira.parse(item))
        return dirots
