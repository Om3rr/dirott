from alchemy import Base, engine
from dira import Dira
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
