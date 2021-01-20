from .base_controller import BaseController
from back_end.dao.dao_category import CategoryDao
from back_end.models.category import Category
import sys
sys.path.append('.')


class CategoryController(BaseController):
    def __init__(self):
        self.__dao = CategoryDao()
        super().__init__(self.__dao, 'Category')
