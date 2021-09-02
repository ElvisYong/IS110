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

print(f"{ten_dollar} ten-dollar bills, {two_dollar} two-dollar bills, {one_dollar} one-dollar bills, {ten_cents} ten-cents coins, and {one_cents} one-cents coins ")