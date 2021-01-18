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
    
    @property
    def identifier(self) -> int:
        return self.__identifier

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email
    
    @property
    def phone(self) -> str:
        return self.__phone