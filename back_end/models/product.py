from sqlalchemy import Column, String, Float
from back_end.models.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = 'products'

    name = Column( String(length = 50) )
    description = Column( String(length = 100) )
    price = Column( String(length=10) )

    def __init__(self, name: str, description: str, price: str):
        self.name = name
        self.description = description
        self.price = price
    
    @property
    def identifier(self) -> int:
        return self.__identifier
    @identifier.setter
    def identifier(self, identifier: int) -> None:
        self.__identifier = identifier

    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description
    @description.setter
    def description(self, description: str) -> None:
        self.__description = description    

    @property
    def price(self) -> float:
        return self.__price
    @price.setter
    def price(self, price: float) -> None:
        self.__price = price