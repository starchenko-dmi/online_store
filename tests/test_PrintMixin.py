from src.class_models import Product


def test_repr_output(capsys):
    """Проверяем, что __repr__ возвращает корректную строку"""
    obj = Product("Тест", "Описание", 100.0, 10)
    captured = capsys.readouterr()
    expected = "Product(Тест, Описание, 100.0, 10)\n"
    assert captured.out == expected


def test_mixin_calls_repr_on_init(capsys):
    """При создании объекта repr должен печататься автоматически"""
    Product("A", "B", 1.0, 1)
    captured = capsys.readouterr()
    assert "Product(A, B, 1.0, 1)" in captured.out
