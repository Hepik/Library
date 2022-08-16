from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Book, Base, MenuItem, Client

engine = create_engine('sqlite:///librarylist.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

Client1 = Client(id=1, name="Robo Barista", email="tinnyTim@udacity.com")
session.add(Client1)
session.commit()
