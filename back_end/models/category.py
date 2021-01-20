from sqlalchemy import Column, String
from .base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'categories'
    name = Column(String(length=50))
    description = Column(String(length=100))

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
