# Name:
# Email ID:

def compute_total_price(price_dict, item_list):
    # Modify the code below.
    total = 0.0
    for item in item_list:
        name, quantity = item
        if name in price_dict:
            price = price_dict[name]
            total += price * quantity

    return total