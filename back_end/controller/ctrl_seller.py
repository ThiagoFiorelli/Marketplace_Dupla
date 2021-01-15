import sys
sys.path.append('.')

from back_end.models.seller import Seller
from back_end.dao.dao_seller import SellerDao
from back_end.controller.base_controller import BaseController

class SellerController(BaseController):
    def __init__(self) -> None:
        self.__dao = SellerDao()
        super().__init__(self.__dao)
