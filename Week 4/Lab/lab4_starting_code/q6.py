## Q6
######################################################################################
# This code is provided to you. DO NOT MODIFY THE CODE!
def calculate_price_after_discount(unit_price, quantity, discount_rate):
    """
    This function takes in the unit price, quantity and discount rate of an item.
    It returns the total price after discount for the item.
    Parameters:
        - unit_price (float): The unit price of the item.
        - quantity (int): The quantity of the item being purchased.
        - discount_rate (float): The percentage of discount. E.g., if there's a 
          10% discount, then discount_rate is set to 10.
    Return:
        - The total price of the item with the specified quantity after discount.
    """
    return (unit_price * quantity * (1 - discount_rate/100))

######################################################################################
# Write your solution below for Part A:
# no_of_items = int(input("How many items do you want to check out? "))
# total_price = 0

# for i in range(no_of_items):
#     print("Enter the details of Item ", i + 1)
#     item = input("What is the item? ")
#     unit_price = float(input("What is the unit price? "))
#     quantity = int(input("What is the quantity ? "))
#     discount = input("Does this item have any discount? [yes|no] ")
#     if discount == "yes":
#         discount_rate = float(input("What is the discount rate? "))
#         total_price += calculate_price_after_discount(unit_price, quantity, discount_rate)
#         continue
#     total_price += unit_price * quantity

# print("The total amount you have to pay is: ", round(total_price, 2))

######################################################################################
# Write your solution below for Part B:

no_of_items = int(input("How many items do you want to check out? "))
original_total_price = 0
discounted_total_price = 0

for i in range(no_of_items):
    print("Enter the details of Item ", i + 1)
    item = input("What is the item? ")
    unit_price = float(input("What is the unit price? "))
    quantity = int(input("What is the quantity ? "))
    discount = input("Does this item have any discount? [yes|no] ")
    original_total_price += unit_price * quantity
    if discount == "yes":
        discount_rate = float(input("What is the discount rate? "))
        discounted_total_price += calculate_price_after_discount(unit_price, quantity, discount_rate)
        continue
    discounted_total_price += unit_price * quantity

print("The total amount you have to pay is:", round(discounted_total_price, 2))
print("You have saved", round(original_total_price - discounted_total_price, 2), "in this transaction.")



