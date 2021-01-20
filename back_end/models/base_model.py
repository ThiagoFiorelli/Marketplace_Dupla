from typing import Tuple
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

base = declarative_base()


class BaseModel(base):
    __abstract__ = True
    identifier = Column(Integer, primary_key=True)

