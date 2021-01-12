import sys
sys.path.append('.')

import back_end.dao.dao_sql_marketplace as dao_ac
import back_end.controller.ctrl_log as ac_log
from ..model.Marketplace import Marketplace

def create_marketplace(mkp:Marketplace)->None:
    dao_ac.add_marketplace(mkp)
    ac_log.save_log(f'Cadastro do marketplace "{mkp.name}" ao database.')

def list_marketplaces()->list:
    marketplaces = dao_ac.read_marketplace()
    ac_log.save_log('Listado todos os marketplaces.')
    return marketplaces
