from back_end.models.baseDao import BaseDao
from back_end.models.product import Product

class ProductDao(BaseDao):
    def create(self, product: Product) -> None:
        name = product.get_name()
        description = product.get_description()
        price = product.get_price()

        query = f"INSERT INTO product (name_prod, description, price) values('{name}','{description}', '{price}');"
        super().execute(query)

    def read(self, search: str = None) -> list[Product]:
        if search == None:
            query = "SELECT * FROM product;"
        else:
            query = f"SELECT * FROM product WHERE name_prod LIKE '%{search}%' OR description LIKE '%{search}%' OR price LIKE '%{search}%';"
        products = []
        list_product = super().read(query)

        for product in list_product:
            product = Product(product[1], product[2], product[3], product[0])
            products.append(product)
        return products
    
    def read_by_id(self, id: int) -> Product:
        query = f"SELECT * FROM product WHERE id = {id};"
        list_product = super().read(query)[0]
        product = Product(list_product[1], list_product[2], list_product[3], list_product[0])
        return product

    def delete(self, id: int) -> None:
        query = f"DELETE FROM product WHERE id = {id};"
        super().execute(query)

    def update(self, id: int, product: Product) -> None:
        name = product.get_name()
        description = product.get_description()
        price = product.get_price()
        query = f"UPDATE product set name_product = '{name}', description = '{description}', price = '{price}' WHERE id = {id};"
        super().execute(query)