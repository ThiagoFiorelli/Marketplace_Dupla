import sys
sys.path.append('.')

import back_end.dao.dao_txt_category as dao_ac_txt
import back_end.dao.dao_log as dao_ac_log

def create_category(name: str, description: str):
    category = f'{name};{description}'
    dao_ac_txt.add_category(category)
    dao_ac_log.generate_log(f'Cadastro da categoria "{name}" ao database.')

def list_categories():
    categories = dao_ac_txt.read_categories()
    dao_ac_log.generate_log('Listado todas as categorias.')
    return categories
