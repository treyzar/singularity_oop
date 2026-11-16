def test_product_init(phone):
    assert phone.name == "Iphone 15"
    assert phone.description == "512GB, Gray space"
    assert phone.price == 210000.0
    assert phone.quantity == 8


def test_product_types(phone):
    assert isinstance(phone.price, float)
    assert isinstance(phone.quantity, int)
