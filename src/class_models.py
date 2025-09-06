from typing import List


class Product:
    """Класс продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс категорий"""

    category_count = 0
    product_count = 0
    name: str
    description: str
    products: List[Product]

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count = len(products)
