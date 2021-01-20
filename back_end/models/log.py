from datetime import datetime
from back_end.models.base_model import BaseModel
from sqlalchemy import String, Column


class Log(BaseModel):
    __tablename__ = 'logs'

    hour = Column(String(length=50))
    date = Column(String(length=50))
    message = Column(String(length=200))

    def __init__(self, message: str, hour: str = None, date: str = None):
        if hour == None:
            self.hour = datetime.now().strftime('%H:%M:%S')
            self.date = datetime.now().strftime('%d/%m/%Y')
        else:
            self.hour = hour
            self.date = date
        self.message = message

