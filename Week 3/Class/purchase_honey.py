from retail_utility import calculate_max_quantity_and_change

amount = float(input("How much money do you want to spend? "))

quantity, change = calculate_max_quantity_and_change(98.50, amount)
remainding_quantity , change = calculate_max_quantity_and_change(58.50, change)
quantity = (quantity * 1000) + (remainding_quantity * 500)
print(f"You can buy {quantity} grams of honey. You have ${change:.2f} left as your change")

