from datetime import datetime

class Log:
    __identifier: int
    __hour: str
    __date: str
    __message: str

    def __init__(self, message: str, hour: str = None, date: str = None, identifier: int = None):
        if hour == None:
            self.hour = datetime.now().strftime('%H:%M:%S')
            self.date = datetime.now().strftime('%d:%m:%Y')
        else:
            self.hour = hour
            self.date = date
        self.message = message
        self.identifier = identifier
    
    @property
    def identifier(self) -> int:
        return self.__identifier
    @identifier.setter
    def identifier(self, identifier: str) -> None:
        self.__identifier = identifier
    
    @property
    def hour(self) -> str:
        return self.__hour
    @hour.setter
    def hour(self, hour: str) -> None:
        self.__hour = hour
    
    @property
    def date(self) -> str:
        return self.__date
    @date.setter
    def date(self, date: str) -> None:
        self.__date = date
    
    @property
    def message(self) -> str:
        return self.__message
    @message.setter
    def message(self, message: str) -> None:
        self.__message = message