# Lab2_Q5
# ########################################
# # lab2_Q5_part1: Write your code below:
def calculate_price_after_discount(unit_price, quantity, discount):
    """
    Calculates the price after discount
    :param unit_price:
    :param quantity:
    :param discount:
    :return:
    """
    # price = unit_price * quantity
    # price = price - (price * (discount/100))
    # return price
    price = unit_price - (unit_price * (discount/100))
    return price * quantity


# ########################################
# lab2_Q5_part2: Write your code below:
milk = calculate_price_after_discount(5.95, 2, 10)
rice = calculate_price_after_discount(6.50, 1, 5)
eggs = calculate_price_after_discount(2.40, 2, 0)
kaya = calculate_price_after_discount(3.95, 3, 15)

total = milk + rice + eggs + kaya
print("The total of your shopping cart after discount is ", total)
