from src.category import Category
from src.category_iterator import CategoryIterator
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone

if __name__ == "__main__":
    product1 = Smartphone("Samsung Galaxy S23 Ultra", "Камера 200 Мп", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    product2 = Smartphone("Iphone 15", "Для связи и фото", 210000.0, 8, 98.2, "15", 512, "Серый космос")
    product3 = Smartphone(
        "Xiaomi Redmi Note 11", "Для повседневных задач", 31000.0, 14, 90.3, "Note 11", 1024, "Синий"
    )

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(product1))
    print(str(product2))
    print(str(product3))
    print(str(category1))
    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    print("Перебор товаров категории:")
    for product in CategoryIterator(category1):
        print(product)

    grass1 = LawnGrass("Газонная трава", "Для дачи", 500.0, 20, "Россия", "7 дней", "Зелёный")
    grass2 = LawnGrass("Спортивный газон", "Для площадки", 700.0, 10, "Россия", "10 дней", "Тёмно-зелёный")
    garden = Category("Для сада", "Семена и инструменты", [grass1])
    garden.add_product(grass2)
    garden.add_product(Product("Лопата", "Садовая", 1200.0, 4))
    print(garden)
    print(garden.products)
    print("Стоимость запасов травы:", grass1 + grass2)

    try:
        print(product1 + grass1)
    except TypeError as error:
        print("Проверяю сложение разных товаров:", error)

    try:
        garden.add_product("Это не товар")  # type: ignore[arg-type]
    except TypeError as error:
        print("Проверяю добавление постороннего объекта:", error)
