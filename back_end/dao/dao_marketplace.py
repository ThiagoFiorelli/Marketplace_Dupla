from ..models.marketplace import Marketplace
from .base_dao import BaseDao

class MarketplaceDao(BaseDao):
    def __init__(self):
        super().__init__(Marketplace)
