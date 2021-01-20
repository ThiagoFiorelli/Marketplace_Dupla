from sqlalchemy import Column, String
from back_end.models.base_model import BaseModel


class Seller(BaseModel): 
    __tablename__ = 'sellers'
    
    name = Column(String(length=100))
    email = Column(String(length=50))
    phone = Column(String(length=15))

    def __init__(self, name:str, email:str, phone:str):
        self.name = name
        self.email = email
        self.phone = phone
    