from back_end.models.category import Category
from back_end.dao.base_dao import BaseDao


class CategoryDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Category)
