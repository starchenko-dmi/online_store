from symtable import Class
from typing import List

from src.BaseProduct import BaseProduct
from src.PrintMixin import PrintMixin


class Product(BaseProduct, PrintMixin):
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
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("сложить можно только объекты класса Product")

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
                    print("Цена осталась без изменений")
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

    def __init__(self, name: str, description: str, products: List[Product] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __len__(self):
        return len(self.__products)

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products_list(self) -> List[Product]:
        """Возвращает список продуктов (для внутреннего использования)"""
        return self.__products

    @property
    def products(self) -> str:
        """Возвращает строковое представление всех продуктов"""
        if not self.__products:
            return "Нет продуктов в категории."
        return "\n".join(str(product) for product in self.__products)


class IterProducts:
    """Класс для итерации по продуктам в категории"""

    def __init__(self, category):
        if not isinstance(category, Category):
            raise TypeError("Данный класс работает только с объектами Category")
        self.category = category

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        products = self.category.products_list  # используем геттер

        if self.current_index < len(products):
            product = products[self.current_index]
            self.current_index += 1
            return product
        else:
            raise StopIteration
