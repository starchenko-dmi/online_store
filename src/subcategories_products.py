from src.class_models import Product


class Smartphone(Product):
    """Класс смартфонов"""
    def __init__(
            self, name: str, description: str, price: float,quantity: int, efficiency: str,
            model: str, memory: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self._Product__price * self.quantity + other._Product__price * other.quantity
        else:
            raise TypeError


class LawnGrass(Product):
    """Класс газонной травы"""
    def __init__(
            self, name: str, description: str, price: float,quantity: int, country: str,
            germination_period: int, color: str) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self._Product__price * self.quantity + other._Product__price * other.quantity
        else:
            raise TypeError



