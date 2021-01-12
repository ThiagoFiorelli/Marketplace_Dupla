class Log:
    __identifier: int
    __hour: str
    __date: str
    __message: str

    def __init__(self, hour: str, date: str, message: str, identifier: int = None):
        self.__hour = hour
        self.__date = date
        self.__message = message
        self.__identifier = identifier
    
    def get_identifier(self) -> int:
        return self.__identifier
    
    def get_hour(self) -> str:
        return self.__hour
    
    def get_date(self) -> str:
        return self.__date
    
    def get_message(self) -> str:
        return self.__message