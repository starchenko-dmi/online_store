import pytest

from src.class_models import Category, IterProducts, Product


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
    """Тест продукта с пустыми строками (но допустимым количеством)"""
    # Пустые строки для name и description допустимы (если нет ограничений в ТЗ)
    product = Product("", "", 100.0, 1)
    assert product.name == ""
    assert product.description == ""
    assert product.price == 100.0
    assert product.quantity == 1


def test_product_zero_quantity_raises_error():
    """Тест, что создание продукта с quantity <= 0 вызывает ValueError"""
    try:
        Product("Товар", "Описание", 100.0, 0)
        assert False, "Expected ValueError was not raised"
    except ValueError as e:
        assert str(e) == "Товар с нулевым количеством не может быть добавлен"

    # Также проверим отрицательное количество
    try:
        Product("Товар", "Описание", 100.0, -5)
        assert False, "Expected ValueError was not raised"
    except ValueError as e:
        assert str(e) == "Товар с нулевым количеством не может быть добавлен"


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


def test_product_str():
    """Тест для метода __str__ класса Product"""
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add():
    """Тест для метода __add__ между двумя продуктами"""
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    total = product1 + product2
    expected = 180000 * 5 + 210000 * 8
    assert total == expected


def test_product_add_type_error():
    """Тест, что __add__ не работает с объектами другого типа"""
    product1 = Product("Samsung", "Описание", 1000.0, 10)
    not_product = "Это не продукт"

    with pytest.raises(TypeError):
        (
            product1 + not_product
        )  # Должно вызвать TypeError, если не реализовано иное поведение


def test_category_str():
    """Тест для метода __str__ класса Category"""
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения фотографий и видео",
        [product1, product2],
    )

    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


def test_iter_products_normal_case():
    """Тест: итерация по нескольким продуктам"""
    p1 = Product("Samsung", "Смартфон", 1000.0, 5)
    p2 = Product("iPhone", "Смартфон", 2000.0, 3)
    p3 = Product("Xiaomi", "Смартфон", 800.0, 7)

    category = Category("Смартфоны", "Все смартфоны", [p1, p2, p3])
    iterator = IterProducts(category)

    products = list(iterator)  # Собираем все продукты в список

    assert len(products) == 3
    assert products[0] == p1
    assert products[1] == p2
    assert products[2] == p3


def test_iter_products_empty_category():
    """Тест: итерация по пустой категории"""
    category = Category("Пустая", "Нет продуктов", [])
    iterator = IterProducts(category)

    products = list(iterator)

    assert len(products) == 0


def test_iter_products_single_product():
    """Тест: итерация по одному продукту"""
    p = Product("Один", "Единственный", 999.9, 1)
    category = Category("Один продукт", "Тест", [p])
    iterator = IterProducts(category)

    products = list(iterator)

    assert len(products) == 1
    assert products[0] == p


def test_iter_products_type_error():
    """Тест: TypeError при передаче не-Category объекта"""
    with pytest.raises(
        TypeError, match="Данный класс работает только с объектами Category"
    ):
        IterProducts("не категория")

    with pytest.raises(TypeError):
        IterProducts(123)

    with pytest.raises(TypeError):
        IterProducts(None)


def test_middle_price_with_one_product():
    """Тест средней цены с одним товаром"""
    product = Product("Товар1", "Описание1", 100.0, 5)
    category = Category("Категория1", "Описание категории", [product])
    assert category.middle_price() == 100.0


def test_middle_price_with_multiple_products():
    """Тест средней цены с несколькими товарами"""
    p1 = Product("Товар1", "Описание1", 100.0, 2)
    p2 = Product("Товар2", "Описание2", 200.0, 3)
    p3 = Product("Товар3", "Описание3", 300.0, 1)
    category = Category("Категория", "Описание", [p1, p2, p3])
    expected = (100.0 + 200.0 + 300.0) / 3
    assert category.middle_price() == expected


def test_middle_price_with_empty_category():
    """Тест средней цены для пустой категории"""
    category = Category("Пустая", "Нет товаров")
    assert category.middle_price() == 0


def test_middle_price_after_adding_product():
    """Тест средней цены после добавления товара через add_product"""
    category = Category("Категория", "Описание")
    assert category.middle_price() == 0

    p1 = Product("Товар", "Описание", 150.0, 10)
    category.add_product(p1)
    assert category.middle_price() == 150.0

    p2 = Product("Товар2", "Описание2", 250.0, 5)
    category.add_product(p2)
    expected = (150.0 + 250.0) / 2  # 200.0
    assert category.middle_price() == expected


def test_iter_products_manual_iteration():
    """Тест: ручной вызов __iter__ и __next__"""
    p1 = Product("Prod1", "Описание", 100.0, 1)
    p2 = Product("Prod2", "Описание", 200.0, 1)
    category = Category("Тест", "Описание", [p1, p2])

    iterator = IterProducts(category)
    iter_obj = iter(iterator)  # вызывает __iter__

    assert next(iter_obj) == p1
    assert next(iter_obj) == p2

    with pytest.raises(StopIteration):
        next(iter_obj)  # Больше нет элементов


def test_iter_products_multiple_iterations():
    """Тест: можно ли итерироваться несколько раз?"""
    p = Product("Тест", "Описание", 500.0, 1)
    category = Category("Тестовая", "Категория", [p])

    iterator = IterProducts(category)

    # Первая итерация
    products1 = list(iterator)
    assert len(products1) == 1

    # Вторая итерация — должна работать снова!
    products2 = list(iterator)
    assert len(products2) == 1
    assert products1[0] == products2[0]
