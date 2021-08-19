number_array = []
number_type = ["Even", "Odd"]

for i in range(0, 4):
  number_array.append(int(input("Enter a number: ")))

for number in number_array:
  print(number_type[number % 2])
