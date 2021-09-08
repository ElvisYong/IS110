no_of_books = int(input("How many books do you have in your basket? "))
i = 0
total_price = 0
books = []
while i < no_of_books:
    price_of_book = float(input("What is the price of the book number " + str(i + 1) + "? "))
    total_price += price_of_book
    books.append(price_of_book)
    i += 1

books.sort()
def binary_search_lower(books):
    lower = 0
    upper = len(books) - 1
    while lower < upper:
        mid = lower + (upper - lower) // 2
        if books[mid] < 10:
            lower = mid + 1
        else:
            upper = mid - 1
    return mid + 1

print("")
print("a) The total price of your books is ", total_price)
# print("The total price of your books is ", sum(books))
print("b) Average prive: " , total_price/no_of_books)
print("c) Price of the least expensive book: " , books[0])
# print("Price of the least expensive book: ", min(books))
print("d) Price of the most expensive book: " , books[len(books)-1])
# print("Price of the most expensive book: ", max(books))
print("e) Number of books cheaper than $10 ", binary_search_lower(books))
print("f) Percentage of books cheaper than $10 " , round(binary_search_lower(books)/no_of_books*100, 2) , "%")