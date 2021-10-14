total = 0
book = float(input("Please pick a book. How much is it (in $)? "))
while total <= 100:
    total += book
    if total > 100:
        break
    print("You still have another " + str(100 - total) + " left to spend.")
    book = float(input("Please pick another book. How much is it (in $) "))

print("You are done!")
print("The total price is $" + str(total))