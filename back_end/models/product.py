class Product:
    __identifier: int
    __name: str
    __description: str
    __price: float

    def __init__(self, name: str, description: str, price: float, identifier: int = None):
        self.__identifier = identifier
        self.__name = name
        self.__description = description
        self.__price = price
    
    @property
    def identifier(self) -> int:
        return self.__identifier

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description
    
    @property
    def price(self) -> float:
        return self.__price