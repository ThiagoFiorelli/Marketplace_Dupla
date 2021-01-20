from datetime import datetime
from back_end.models.base_model import BaseModel
from sqlalchemy import String, Column


class Log(BaseModel):
    __tablename__ = 'log'

    hora = Column(String(length=50))
    data = Column(String(length=50))
    mensagem = Column(String(length=200))

    def __init__(self, mensagem: str, hora: str = None, data: str = None):
        if hora == None:
            self.hora = datetime.now().strftime('%H:%M:%S')
            self.data = datetime.now().strftime('%d/%m/%Y')
        else:
            self.hora = hora
            self.data = data
        self.mensagem = mensagem

