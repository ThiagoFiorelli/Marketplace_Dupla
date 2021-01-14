class Category:
    __id: int
    __name: str
    __description: str

    def __init__(self, name:str, description:str):
        self.__name = name
        self.__description = description

    @property
    def id(self)->int:
        return self.__id
    
    @id.setter
    def id(self, id:int)->None:
        self.__id = id

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
