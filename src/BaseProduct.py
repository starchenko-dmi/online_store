from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс с методом сложения"""

    @abstractmethod
    def __add__(self, other):
        pass
