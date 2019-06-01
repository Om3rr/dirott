from sqlalchemy import Sequence
from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime
from alchemy import Base
import re
class Dira(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    hood = Column(String)
    hood_id = Column(Integer)
    street = Column(String)
    home_id = Column(String)
    price = Column(Integer)
    size = Column(Integer)
    rooms = Column(Integer)
    floor = Column(Integer)
    merchant = Column(String)


    def href(self):
        return "https://yad2.co.il/item/{}".format(self.id)

    def from_tivuch(self):
        return self.merchant != None

    def to_telegram(self):
        return '''
        *{tivuch}*
        מצאנו {home_id} ב*{hood}* ברחוב *{street}*
        המחיר הוא *{price}*
        גודל *{size}* מ"ר ובקומה *{floor}*
        בדירה יש *{rooms}* חדרים
        {href}
        '''.format(street=self.street, hood=self.hood, price=self.price, floor=self.floor, size=self.size,
                   rooms=self.rooms, href=self.href(), home_id=self.home_id, tivuch=("מתיווך" if self.from_tivuch() else ""))
    @staticmethod
    def parse(item):
        hood = item.get("neighborhood")
        street = "{} {}".format(item.get("street"), item.get("address_home_number"))
        price = int(re.sub("[^\d]", '', item.get("price")))
        size = item.get("square_meters")
        rooms = item.get("Rooms_text")
        floor = item.get("TotalFloor_text")
        home_id = item.get("HomeTypeID_text")
        merchant = item.get("merchant_name")
        return Dira(id=item.get('id'), hood=hood,
                    street=street, rooms=rooms,
                    price=price, size=size,
                    floor=floor, home_id=home_id,
                    merchant=merchant
                    )


    @staticmethod
    def relevant(item):
        return item.get('id') != None
