import sys
sys.path.append('.')

import back_end.dao.dao_sql_category as dao_ac_txt
import back_end.controller.ctrl_log as ac_log

def create_category(name: str, description: str):
    category = f'{name};{description}'
    dao_ac_txt.add_category(category)
    ac_log.save_log(f'Cadastro da categoria "{name}" ao database.')

def list_categories():
    categories = dao_ac_txt.read_categories()
    ac_log.save_log('Listado todas as categorias.')
    return categories
