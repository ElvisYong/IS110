# Part I
item = input("Do you have any item left in your shopping cart? Please enter Y or N: ")
total_price = 0
while item == "Y":
    name = input("Please enter the name of the item : ")
    price = float(input("Please enter the price of the item : "))
    quantity = int(input("Please enter the quantity of the item : "))
    total_price += (price * quantity)
    item = input("Do you have any item left in your shopping cart? Please enter Y or N: ")

print("Total price: $" + str(total_price))

# Part II
item = input("Do you have any item left in your shopping cart? Please enter Y or N: ")
storage = []
total_price = 0
while item == "Y":
    name = input("Please enter the name of the item : ")
    price = float(input("Please enter the price of the item : "))
    quantity = int(input("Please enter the quantity of the item : "))
    total_price += (price * quantity)
    storage.append((name, price, quantity))
    item = input("Do you have any item left in your shopping cart? Please enter Y or N: ")

print("You have entered the following items:")
for i in storage:
    print(f"{i[0]} ${i[1]} {i[2]}")

print("Total price: $" + str(total_price))