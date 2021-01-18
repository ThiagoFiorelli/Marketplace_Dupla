class Seller:
    __identifier: int
    __name: str
    __email: str
    __phone: str

    def __init__(self, name: str, email: str, phone: str, identifier: int = None):
        self.identifier = identifier
        self.name = name
        self.email = email
        self.phone = phone
    
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
    def email(self) -> str:
        return self.__email
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email
    
    @property
    def phone(self) -> str:
        return self.__phone
    @phone.setter
    def phone(self, phone: str) -> None:
        self.__phone = phone