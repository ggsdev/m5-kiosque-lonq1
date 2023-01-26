from menu import products


def calculate_tab(list_dicts_table):
    sum = 0

    for table in list_dicts_table:
        for product in products:
            if product["_id"] == table["_id"]:
                sum += product["price"] * table["amount"]

    return {"subtotal": f"${round(sum, 2)}"}
