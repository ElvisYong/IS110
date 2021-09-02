def get_discount_rate(num_boxes):
    if num_boxes >= 5:
        return 0.2
    elif num_boxes >= 2 and num_boxes <= 4:
        return 0.1
    else:
        return 0.0


def calculate_total_amount(brand, num_boxes):
    if brand == "Tung Lok":
        discount = (55.40 * num_boxes) * get_discount_rate(num_boxes)
        return (55.40 * num_boxes) - discount
    elif brand == "Man Fu Yuan":
        discount = (59.60 * num_boxes) * get_discount_rate(num_boxes)
        return (59.60 * num_boxes) - discount
    else:
      return "No such brand"

brand = input("Which brand do you want to buy? ")
number = float(input("How many boxes do you want to buy? "))

print("You need to pay $", calculate_total_amount(brand, number))