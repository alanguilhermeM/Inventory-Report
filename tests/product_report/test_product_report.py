from inventory_report.product import Product


def test_product_report() -> None:
    instance = Product(
        "2", "book", "livraria", "20/04/2001", "20/04/2003", "DAF8DJ2", "non"
    )

    expected_output = (
        "The product 2 - book with serial number DAF8DJ2 manufactured on "
        "20/04/2001 by the company livraria valid until 20/04/2003 must be "
        "stored according to the following instructions: non."
    )
    assert instance.__str__() == expected_output
