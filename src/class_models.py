from symtable import Class
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
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        else:
            if self.__price > price:
                result = input(
                    'Цена понизилась внести изменения? "y" (значит yes) или "n" (значит no)'
                )
                if result.strip().lower() == "y":
                    self.__price = price
                    return
                else:
                    print("Цена осталась без именений")
                    return
            else:
                self.__price = price
                return

    @classmethod
    def new_product(cls, dictionary: dict) -> Class:
        """Создание экземпляра Product из словаря"""
        name = dictionary.get("name")
        description = dictionary.get("description")
        price = dictionary.get("price")
        quantity = dictionary.get("quantity")
        result = cls(name, description, price, quantity)
        return result


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
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, products: Product):
        self.__products.append(products)
        Category.product_count += 1

    @property
    def products(self) -> str:
        for product in self.__products:
            print(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return
