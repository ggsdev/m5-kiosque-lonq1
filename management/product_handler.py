from menu import products


def get_product_by_id(id: int):
    if type(id) != int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product
    
    return {}


def get_products_by_type(product_type: str):
    if type(product_type) != str:
        raise TypeError("product type must be a str")
    result = []
    for product in products:
        if product["type"] == product_type:
            result.append(product)

    return result


def add_product(menu: list, **kwargs):
    result_product = {}
    for key, value in kwargs.items():
        result_product[key] = value

    if len(menu) == 0:
        new_id = 0
    else:
        new_id = menu[0]["_id"]

    for product in menu:
        if product["_id"] >= new_id:
            new_id = product["_id"]

    result_product["_id"] = new_id + 1

    menu.append(result_product)
    return result_product


def menu_report():
    product_quantity = len(products)
    sum = 0
    count_of_type = 0
    all_types = [type_product["type"] for type_product in products]

    for product in products:
        sum += product["price"]
        frequency = all_types.count(product["type"])
        if frequency > count_of_type:
            count_of_type = frequency
            most_repeated_type = product["type"]

    average_price = round(sum / product_quantity, 2)
    return f"Products Count: {product_quantity} - Average Price: ${average_price} - Most Common Type: {most_repeated_type}"