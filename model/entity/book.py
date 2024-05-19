from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base
from model.entity.person import Person


class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)

    # Relationship
    writer_id = Column(Integer, ForeignKey("person.id"))
    writer = relationship(Person)

    def __init__(self, id, name, writer):
        self.id = id
        self.name = name
        self.writer = writer

