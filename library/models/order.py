from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from library.base.base import Base


class Order(Base):
    __tablename__ = 'orders'
    user_id = Column(Integer, ForeignKey("user.id"))
    librarian_id = Column(Integer, ForeignKey("librarian.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    email_address = Column(String, nullable=False)
    order_date = Column('order_date', Integer)
    return_date = Column('return_date', Integer)
