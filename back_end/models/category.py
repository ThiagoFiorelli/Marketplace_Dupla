class Category:
    __identifier: int
    __name: str
    __description: str

    def __init__(self, name:str, description:str, identifier: int = None):
        self.__name = name
        self.__description = description
        self.__identifier = identifier

    @property
    def identifier(self)->int:
        return self.__identifier
    
    @identifier.setter
    def identifier(self, identifier:int)->None:
        self.__identifier = identifier

    @property
    def name(self)->str:
        return self.__name
    
    @name.setter
    def name(self, name:str)->None:
        self.__name = name

    @property
    def description(self)->str:
        return self.__description

    @description.setter
    def description(self, description:str)->None:
        self.__description = description

    def __str__(self)->str:
        return f'{self.name};{self.description}'
