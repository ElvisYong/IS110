from retail_utility import calculate_max_quantity_and_change

amount = float(input("How much money do you want to spend? "))

if amount >= 98.50:
    quantity, change = calculate_max_quantity_and_change(98.50, amount)
    quantity = quantity * 1000
    if change > 58.50:
        remainding_quantity , change = calculate_max_quantity_and_change(58.50, change)
        quantity = quantity + (remainding_quantity * 500)
    print(f"You can buy {quantity} grams of honey. You have ${change:.2f} left as your change")
else:
    quantity, change = calculate_max_quantity_and_change(58.50, amount)
    print(f"You can buy {quantity * 500} grams of honey. You have ${change:.2f} left as your change")
