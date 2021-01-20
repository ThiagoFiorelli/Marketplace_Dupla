from sqlalchemy import Column, String
from back_end.models.base_model import BaseModel


class Marketplace(BaseModel):
    __tablename__ = 'marketplaces'

    name = Column(String(length=200))
    description = Column(String(length=200))

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self) -> str:
        return f'{self.name};{self.description}'
