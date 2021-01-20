from back_end.models.marketplace import Marketplace
from back_end.dao.base_dao import BaseDao


class MarketplaceDao(BaseDao):
    def __init__(self):
        super().__init__(Marketplace)
