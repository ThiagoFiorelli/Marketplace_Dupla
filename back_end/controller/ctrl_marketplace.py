import sys
sys.path.append('.')

from .base_controller import BaseController
from back_end.dao.dao_sql_category import CategoryDao

class CategoryController(BaseController):
    def __init__(self):
        self.__dao = CategoryDao()
        super().__init__(self.__dao)

# import sys
# sys.path.append('.')

# import back_end.dao.dao_sql_marketplace as dao_ac
# import back_end.controller.ctrl_log as ac_log
# from ..models.Marketplace import Marketplace

# def create_marketplace(mkp:Marketplace)->None:
#     dao_ac.add_marketplace(mkp)
#     ac_log.create_log(f'Cadastro do marketplace "{mkp.name}" ao database.')

# def list_marketplaces()->list:
#     marketplaces = dao_ac.read_marketplaces()
#     ac_log.create_log('Listado todos os marketplaces.')
#     return marketplaces

# def get_by_id(id:int)->Marketplace:
#     return dao_ac.search_by_id(id)

# def update_marketplace(id:int, info):
#     mkp = get_by_id(id)
#     mkp.name = info.get('name')
#     mkp.description = info.get('description')
#     dao_ac.update(mkp)
#     ac_log.create_log(f'Alterando informações de marketplace com id "{id}".') 

# def delete_marketplace(id:int):
#     mkp = get_by_id(id)
#     dao_ac.delete(mkp)
#     ac_log.create_log(f'Deletando marketplace com id "{id}".')
