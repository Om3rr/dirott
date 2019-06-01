from sqlalchemy import Integer, Column, create_engine, ForeignKey, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime
Base = declarative_base()
engine = create_engine('sqlite:///dirot.sqlite', echo=True)
session = None






