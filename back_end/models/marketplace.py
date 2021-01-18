class Marketplace:
    __identifier: int
    __name: str
    __description: str

    def __init__(self, name:str, description:str, identifier: int = None):
        self.__name = name
        self.__description = description
        self.__id = identifier

    @property
    def identifier(self)->int:
        return self.__id
    
    @identifier.setter
    def identifier(self, identifier:int)->None:
        self.__id = identifier

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