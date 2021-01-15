from ctrl_log import LogController

class BaseController:
    def __init__(self, dao, tipo:str)->None:
        self.__dao = dao
        self.__tipo = tipo
        self.__log = LogController()

    def create(self, model: object)->None:
        self.__dao.create(model)
        self.__log.create(f'Cadastro de {self.__tipo}: "{model.name}" na database.')
        

    def read_by_id(self,id:int)-> object:
        lista = self.__dao.read_by_id(id)
        self.__log.create(f'Listagem de {self.__tipo} de id {id} da database.')
        return lista

    def read_all(self)->list:
        lista = self.__dao.read_all()
        self.__log.create(f'Listagem de {self.__tipo} da database.')
        return lista

    def delete(self, id:int)->None:
        self.__dao.delete(id)
        self.__log.create(f'Deletando {self.__tipo} com id "{id}".')

    def update(self, model: object)->None:
        self.__dao.update(model)
        self.__log.create(f'Alterando informações de {self.__tipo} com id "{model.id}".')