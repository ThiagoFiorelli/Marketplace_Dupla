import sys
sys.path.append('.')

from back_end.dao.dao_category import CategoryDao
from .base_controller import BaseController


class CategoryController(BaseController):
    def __init__(self):
        self.__dao = CategoryDao()
        super().__init__(self.__dao, "Categoria")
