import pytest

from src.class_models import Category, Product


@pytest.fixture
def sample_products():
    """Фикстура с тестовыми продуктами"""
    return [
        Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        ),
        Product("iPhone 14 Pro", "128GB, Gold", 150000.0, 3),
        Product("Xiaomi Redmi Note 12", "256GB, Blue", 25000.0, 10),
    ]


def test_product_initialization():
    """Тест инициализации продукта"""
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )

    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_property():
    """Тест геттера цены"""
    product = Product("Телефон", "Описание", 10000.0, 3)
    assert product.price == 10000.0


def test_set_valid_price():
    """Тест установки корректной цены"""
    product = Product("Телефон", "Описание", 10000.0, 3)
    product.price = 15000.0
    assert product.price == 15000.0


def test_set_negative_price(capsys):
    """Тест установки отрицательной цены"""
    product = Product("Телефон", "Описание", 10000.0, 3)
    product.price = -5000.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 10000.0  # Цена не изменилась


def test_set_zero_price(capsys):
    """Тест установки нулевой цены"""
    product = Product("Телефон", "Описание", 10000.0, 3)
    product.price = 0.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 10000.0  # Цена не изменилась


def test_price_increase_no_confirmation_needed():
    """Тест повышения цены без подтверждения"""
    product = Product("Телефон", "Описание", 10000.0, 3)
    product.price = 12000.0
    assert product.price == 12000.0


def test_new_product_from_dictionary():
    """Тест создания продукта из словаря"""
    product_data = {
        "name": "iPhone 14",
        "description": "128GB, Black",
        "price": 90000.0,
        "quantity": 10,
    }

    product = Product.new_product(product_data)

    assert product.name == "iPhone 14"
    assert product.description == "128GB, Black"
    assert product.price == 90000.0
    assert product.quantity == 10


def test_new_product_from_dictionary_missing_fields():
    """Тест создания продукта из словаря с отсутствующими полями"""
    product_data = {
        "name": "iPhone 14",
        "price": 90000.0,
        # description и quantity отсутствуют
    }

    product = Product.new_product(product_data)

    assert product.name == "iPhone 14"
    assert product.price == 90000.0


def test_category_initialization(sample_products):
    """Тест инициализации категории"""
    category = Category("Смартфоны", "Смартфоны и мобильные телефоны", sample_products)

    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны и мобильные телефоны"
    assert len(category._Category__products) == 3  # Приватный атрибут


def test_category_count_increment(sample_products):
    """Тест увеличения счетчика категорий"""
    initial_count = Category.category_count

    category1 = Category("Категория 1", "Описание 1", sample_products[:1])
    category2 = Category("Категория 2", "Описание 2", sample_products[1:2])

    assert Category.category_count == initial_count + 2


def test_product_count_increment(sample_products):
    """Тест увеличения счетчика продуктов"""
    initial_count = Category.product_count

    category = Category("Смартфоны", "Описание", sample_products)

    assert Category.product_count == initial_count + 3


def test_add_product(sample_products):
    """Тест добавления продукта в категорию"""
    category = Category("Смартфоны", "Описание", sample_products[:2])
    new_product = sample_products[2]

    initial_product_count = len(category._Category__products)
    category.add_product(new_product)

    assert len(category._Category__products) == initial_product_count + 1
    assert category._Category__products[-1] == new_product


def test_products_property_output(sample_products, capsys):
    """Тест вывода продуктов через property"""
    category = Category("Смартфоны", "Описание", sample_products)

    # Вызываем property products
    category.products

    captured = capsys.readouterr()
    output = captured.out

    # Проверяем, что информация о продуктах выведена
    assert "Samsung Galaxy S23 Ultra" in output
    assert "180000.0 руб. Остаток: 5 шт." in output
    assert "iPhone 14 Pro" in output
    assert "150000.0 руб. Остаток: 3 шт." in output
    assert "Xiaomi Redmi Note 12" in output
    assert "25000.0 руб. Остаток: 10 шт." in output


@pytest.mark.parametrize(
    "price_input,expected_message",
    [
        (-1000.0, "Цена не должна быть нулевая или отрицательная"),
        (0.0, "Цена не должна быть нулевая или отрицательная"),
        (-0.1, "Цена не должна быть нулевая или отрицательная"),
    ],
)
def test_invalid_prices(capsys, price_input, expected_message):
    """Параметризованный тест для некорректных цен"""
    product = Product("Тестовый продукт", "Описание", 1000.0, 1)
    product.price = price_input

    captured = capsys.readouterr()
    assert expected_message in captured.out


def test_product_with_empty_strings():
    """Тест продукта с пустыми строками"""
    product = Product("", "", 100.0, 0)
    assert product.name == ""
    assert product.description == ""
    assert product.price == 100.0
    assert product.quantity == 0


def test_category_with_empty_products_list():
    """Тест категории с пустым списком продуктов"""
    category = Category("Пустая категория", "Описание", [])
    assert category.name == "Пустая категория"
    assert len(category._Category__products) == 0
    assert Category.product_count >= 0  # Не уменьшается при пустом списке


def test_product_price_with_very_small_values():
    """Тест цены с очень маленькими значениями"""
    product = Product("Тест", "Описание", 0.001, 1)
    assert product.price == 0.001


def test_product_price_with_very_large_values():
    """Тест цены с очень большими значениями"""
    product = Product("Тест", "Описание", 999999999.99, 1)
    assert product.price == 999999999.99


def test_category_products_property_returns_none():
    """Тест, что property products возвращает None"""
    category = Category("Тест", "Описание", [])
    result = category.products
    assert result is None  # Так как функция не возвращает значение


def test_product_str():
    """Тест для метода __str__ класса Product"""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add():
    """Тест для метода __add__ между двумя продуктами"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    total = product1 + product2
    expected = 180000 * 5 + 210000 * 8
    assert total == expected


def test_product_add_type_error():
    """Тест, что __add__ не работает с объектами другого типа"""
    product1 = Product("Samsung", "Описание", 1000.0, 10)
    not_product = "Это не продукт"

    with pytest.raises(TypeError):
        product1 + not_product  # Должно вызвать TypeError, если не реализовано иное поведение


def test_category_str():
    """Тест для метода __str__ класса Category"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны",
                        "Смартфоны, как средство не только коммуникации, но и получения фотографий и видео",
                        [product1, product2])

    assert str(category) == "Смартфоны, количество продуктов: 13 шт."