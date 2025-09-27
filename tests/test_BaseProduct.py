import pytest

from src.BaseProduct import BaseProduct
from src.class_models import Product

# === Тесты для BaseProduct ===


def test_base_product_is_abstract():
    """BaseProduct нельзя инстанцировать напрямую"""
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        BaseProduct()


def test_product_inherits_base_product():
    """Product должен быть подклассом BaseProduct"""
    assert issubclass(Product, BaseProduct)


def test_product_implements_add():
    """Product должен реализовывать __add__"""
    p1 = Product("Товар1", "Описание1", 100, 2)
    p2 = Product("Товар2", "Описание2", 200, 3)
    result = p1 + p2
    assert result == 100 * 2 + 200 * 3  # 800
