from alchemy import engine
from Scraper import Scraper
from sqlalchemy.orm import sessionmaker
from dira import Dira
from telegramer import send_dira
from dirot_filters import FILTERS


def get_and_send_dira(fil):
    dirot = scraper.get_dirot(**fil)
    ids = session.query(Dira.id).filter(Dira.id.in_(map(lambda x: x.id, dirot))).all()
    avail = [x[0] for x in ids]
    for dira in dirot:
        if dira.id not in avail:
            session.add(dira)
            send_dira(dira)
    session.commit()


if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()
    scraper = Scraper()
    for fil in FILTERS:
        get_and_send_dira(fil)

