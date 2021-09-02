change = float(input("What is the change? "))
ten_dollar = int(change // 10)
change = change % 10
two_dollar = int(change // 2)
change = change % 2
one_dollar = int(change // 1)
change = change % 1
ten_cents = int(change // 0.1)
change = change % 0.1
one_cents = int(change // 0.01)


if ten_dollar > 0:
    print("$10 dollar bills:", ten_dollar)
if two_dollar > 0:
    print("$2 dollar bills:", two_dollar)
if one_dollar > 0:
    print("$1 dollar bills:", one_dollar)
if ten_cents > 0:
    print("10 cents:", ten_cents)
if one_cents > 0:
    print("1 cent:", one_cents)