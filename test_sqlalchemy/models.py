from sqlalchemy import Column, ForeignKey, Integer, MetaData, String, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Language(Base):
    __tablename__ = "language"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    extension = Column(String)

    def __init__(self, name, extension):
        self.name = name
        self.extension = extension
