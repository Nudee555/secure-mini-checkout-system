def get_products():
    return [
        {"id": 1, "name": "Laptop", "price": 1000},
        {"id": 2, "name": "Mouse", "price": 25},
        {"id": 3, "name": "Keyboard", "price": 45}
    ]
def get_product_by_id(product_id):
    for product in get_products():
        if product["id"] == product_id:
            return product
    return None

def is_valid_price(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return False
    return product["price"] > 0