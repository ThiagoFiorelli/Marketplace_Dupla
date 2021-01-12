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
    
    def get_identifier(self) -> int:
        return self.__identifier

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description
    
    def get_price(self) -> float:
        return self.__price