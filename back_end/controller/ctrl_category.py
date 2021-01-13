import sys
sys.path.append('.')

import back_end.dao.dao_sql_category as dao_ac
import back_end.controller.ctrl_log as ac_log
from ..models.Category import Category

def create_category(cat: Category)->None:
    dao_ac.add_category(cat)
    ac_log.create_log(f'Cadastro da categoria "{cat.name}" ao database.')

def list_categories()->list:
    categories = dao_ac.read_categories()
    ac_log.create_log('Listado todas as categorias.')
    return categories

def get_by_id(id:int)->Category:
    return dao_ac.search_by_id(id)

def update_category(id:int, info):
    cat = get_by_id(id)
    cat.name = info.get('name')
    cat.description = info.get('description')
    dao_ac.update(cat)
    ac_log.create_log(f'Alterando informações de categoria com id "{id}".') 


def delete_category(id:int):
    cat = get_by_id(id)
    dao_ac.delete(cat)
    ac_log.create_log(f'Deletando categoria com id "{id}".')
