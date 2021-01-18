from back_end.dao.base_dao import BaseDao
from back_end.models.product import Product

class ProductDao(BaseDao):
    def create(self, product: Product) -> None:
        name = product.name
        description = product.description
        price = product.price

        query = f"INSERT INTO products (name_prod, description, price) values('{name}','{description}', {price});"
        super().execute(query)

    def read_all(self, search: str = None) -> list[Product]:
        if search == None:
            query = "SELECT * FROM products;"
        else:
            query = f"SELECT * FROM products WHERE name_prod LIKE '%{search}%' OR description LIKE '%{search}%';"
        products = []
        list_product = super().read_all(query)

        for product in list_product:
            product = Product(product[1], product[2], product[3], product[0])
            products.append(product)
        return products
    
    def read_by_id(self, id: int) -> Product:
        query = f"SELECT * FROM products WHERE id = {id};"
        list_product = super().read_all(query)[0]
        price = float(list_product[3].strip("$"))
        product = Product(list_product[1], list_product[2], price, list_product[0])
        return product

    def delete(self, id: int) -> None:
        query = f"DELETE FROM products WHERE id = {id};"
        super().execute(query)

    def update(self, product: Product) -> None:
        id = product.identifier
        name = product.name
        description = product.description
        price = product.price
        query = f"UPDATE products set name_prod = '{name}', description = '{description}', price = '{price}' WHERE id = {id};"
        super().execute(query)