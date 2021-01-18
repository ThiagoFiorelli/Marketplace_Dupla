class Product:
    __identifier: int
    __name: str
    __description: str
    __price: float

    def __init__(self, name: str, description: str, price: float, identifier: int = None):
        self.identifier = identifier
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