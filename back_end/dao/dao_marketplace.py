from ..models.marketplace import Marketplace
from .base_dao import BaseDao

class MarketplaceDao(BaseDao):
    def create(self, model:Marketplace) -> None:
        query = f"INSERT INTO marketplaces (name_mktplaces, description) values('{model.name}','{model.description}');"
        super().execute(query)

    def read_by_id(self, id:int)->Marketplace:
        query = f"SELECT * FROM marketplaces WHERE id={id};"
        result = super().read(query)[0]
        mkp = Marketplace(result[1], result[2], result[0])
        return mkp

    def read_all(self)->list:
        query = f"SELECT * FROM marketplaces;"
        result_list = super().read(query)
        marketplaces = []
        for result in result_list:
            mkp = Marketplace(result[1], result[2], result[0])
            marketplaces.append(mkp)
        return marketplaces
    
    def delete(self, id:int)->None:
        query = f"DELETE FROM marketplaces WHERE id={id};"
        super().execute(query)

    def update(self, model:Marketplace)->None:
        print(model)
        query = f"UPDATE marketplaces SET name_mktplaces='{model.name}', description='{model.description}' WHERE id={model.identifier};"
        super().execute(query)
