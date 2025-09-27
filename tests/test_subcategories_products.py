import pytest

from src.class_models import Product
from src.subcategories_products import LawnGrass, Smartphone

# --- Тесты для Smartphone ---


def test_smartphone_creation():
    """Проверка создания объекта Smartphone"""
    phone = Smartphone(
        name="iPhone 15",
        description="Latest iPhone",
        price=999.99,
        quantity=5,
        efficiency="High",
        model="15",
        memory=256,
        color="Black",
    )

    assert phone.name == "iPhone 15"
    assert phone.price == 999.99
    assert phone.quantity == 5
    assert phone.efficiency == "High"
    assert phone.model == "15"
    assert phone.memory == 256
    assert phone.color == "Black"


def test_smartphone_addition():
    """Проверка сложения двух смартфонов"""
    phone1 = Smartphone("iPhone", "", 1000, 2, "", "", 0, "")
    phone2 = Smartphone("Samsung", "", 800, 3, "", "", 0, "")

    result = phone1 + phone2
    assert result == 1000 * 2 + 800 * 3  # 2000 + 2400 = 4400


def test_smartphone_addition_with_wrong_type():
    """Проверка, что TypeError возникает при сложении с другим типом"""
    phone = Smartphone("iPhone", "", 1000, 1, "", "", 0, "")
    grass = LawnGrass("Газон", "", 50, 10, "", 0, "")

    with pytest.raises(TypeError):
        phone + grass


# --- Тесты для LawnGrass ---


def test_lawn_grass_creation():
    """Проверка создания объекта LawnGrass"""
    grass = LawnGrass(
        name="Premium Grass",
        description="Fast growing",
        price=25.5,
        quantity=100,
        country="Russia",
        germination_period=7,
        color="Green",
    )

    assert grass.name == "Premium Grass"
    assert grass.price == 25.5
    assert grass.quantity == 100
    assert grass.country == "Russia"
    assert grass.germination_period == 7
    assert grass.color == "Green"


def test_lawn_grass_addition():
    """Проверка сложения двух газонов"""
    grass1 = LawnGrass("Газон1", "", 10, 50, "", 0, "")
    grass2 = LawnGrass("Газон2", "", 15, 30, "", 0, "")

    result = grass1 + grass2
    assert result == 10 * 50 + 15 * 30  # 500 + 450 = 950


def test_lawn_grass_addition_with_wrong_type():
    """Проверка, что TypeError возникает при сложении с другим типом"""
    grass = LawnGrass("Газон", "", 10, 1, "", 0, "")
    phone = Smartphone("iPhone", "", 1000, 1, "", "", 0, "")

    with pytest.raises(TypeError):
        grass + phone


def test_is_instance_of_product():
    """Проверка, что объекты наследуются от Product"""
    phone = Smartphone("Test", "", 1, 1, "", "", 0, "")
    grass = LawnGrass("Test", "", 1, 1, "", 0, "")

    assert isinstance(phone, Product)
    assert isinstance(grass, Product)
