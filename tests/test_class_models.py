import pytest

from src.class_models import Category, Product


@pytest.fixture
def product1():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    return product1


@pytest.fixture
def category1():
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни",
        ["product1", "product2", "product3", "product4"],
    )
    return category1


def test_init_product(product1):
    """Тест инициализации класса Product"""
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_init_category(category1):
    """Тест инициализации класса Category"""
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category1.products == ["product1", "product2", "product3", "product4"]

    """Тест количества продуктов в категории и количества категорий"""
    assert category1.category_count == 1
    assert category1.product_count == 4
