from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    count = Column(Integer, primary_key=True)
    carriers = Column(String(250), nullable=False)

    # JSON
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class MenuItem(Base):
    __tablename__ = 'list_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    library_id = Column(Integer, ForeignKey('library.id'))
    book = relationship(Book)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Client)

    # JSON
    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
        }


engine = create_engine('sqlite:///librarylist.db')
Base.metadata.create_all(engine)
