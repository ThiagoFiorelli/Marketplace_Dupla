from datetime import datetime

class Log:
    __identifier: int
    __hour: str
    __date: str
    __message: str

    def __init__(self, message: str, hour: str = None, date: str = None, identifier: int = None):
        if hour == None:
            self.__hour = datetime.now().strftime('%H:%M:%S')
            self.__date = datetime.now().strftime('%d:%m:%Y')
        else:
            self.__hour = hour
            self.__date = date
        self.__message = message
        self.__identifier = identifier
    
    @property
    def identifier(self) -> int:
        return self.__identifier
    
    @property
    def hour(self) -> str:
        return self.__hour
    
    @property
    def date(self) -> str:
        return self.__date
    
    @property
    def message(self) -> str:
        return self.__message