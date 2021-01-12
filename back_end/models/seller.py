class Seller:
    __identifier: int
    __name: str
    __email: str
    __phone: str

    def __init__(self, name: str, email: str, phone: str, identifier: int = None):
        self.__identifier = identifier
        self.__name = name
        self.__email = email
        self.__phone = phone
    
    def get_identifier(self) -> int:
        return self.__identifier

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email
    
    def get_phone(self) -> str:
        return self.__phone