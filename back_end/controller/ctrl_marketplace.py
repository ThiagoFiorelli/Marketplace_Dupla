import sys
sys.path.append('.')

from back_end.dao.dao_marketplace import MarketplaceDao
from .base_controller import BaseController

class MarketplaceController(BaseController):
    def __init__(self):
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao, "Marketplace")
