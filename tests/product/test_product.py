from inventory_report.product import Product


def test_create_product() -> None:
    instance = Product(
        "2", "book", "livraria", "20/04/2001", "20/04/2003", "DAF8DJ2", "non"
    )

    assert instance.id == '2'
    assert instance.product_name == 'book'
    assert instance.company_name == 'livraria'
    assert instance.manufacturing_date == '20/04/2001'
    assert instance.expiration_date == '20/04/2003'
    assert instance.serial_number == 'DAF8DJ2'
    assert instance.storage_instructions == 'non'
