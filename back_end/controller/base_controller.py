from back_end.models.base_model import BaseModel
from .ctrl_log import LogController


class BaseController:
    def __init__(self, dao, tipo: str) -> None:
        self.__dao = dao()
        self.__tipo = tipo
        self.__log = LogController()

    def save(self, model: BaseModel) -> None:
        self.__dao.save(model)
        self.__log.create(f'Cadastro de {self.__tipo} na database.')

    def read_by_id(self, id: int) -> BaseModel:
        obj = self.__dao.read_by_id(id)
        self.__log.create(f'Listagem de {self.__tipo} de id {id} da database.')
        return obj

    def read_all(self) -> list:
        lista = self.__dao.read_all()
        self.__log.create(f'Listagem de {self.__tipo} da database.')
        return lista

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)
        self.__log.create(f'Deletando {self.__tipo} com id "{model.id}".')
