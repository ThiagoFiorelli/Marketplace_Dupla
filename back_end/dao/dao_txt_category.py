from ..model.Category import Category

categories_db = 'data/categories.txt'

def add_category(category: Category) -> None:
    with open(categories_db, 'a', encoding='utf-8') as categories_file:
        categories_file.write(f'{category}\n')


def read_categories() -> list:
    with open(categories_db, 'r', encoding='utf-8') as categories_file:
        categories = []
        for category in categories_file:
            name, description = category.strip().split(';')
            cat = Category(name, description)
            categories.append(cat)
    return categories