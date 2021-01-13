import sys
sys.path.append('.')

import back_end.dao.dao_sql_category as dao_ac
import back_end.controller.ctrl_log as ac_log
from ..model.Category import Category

def create_category(cat: Category)->None:
    dao_ac.add_category(cat)
    ac_log.create_log(f'Cadastro da categoria "{cat.name}" ao database.')

def list_categories()->list:
    categories = dao_ac.read_categories()
    ac_log.create_log('Listado todas as categorias.')
    return categories
