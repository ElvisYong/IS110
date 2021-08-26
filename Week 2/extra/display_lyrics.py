def pear_tree():
  print("A partridge in a pear tree")
  print()

def first(n):
  print(f"On the {n} day of Christmas my true love gave to me")

def second():
  first("second")
  print("Two turtle doves, and")

def third():
  first("third")
  print("Three French hens")
  second()

def fourth():
  first("fourth")
  print("Four colly birds")
  third()
  second()

def fifth():
  first("fifth")
  print("Five gold rings")
  fourth()
  third()
  second()

def sixth():
  first("sixth")
  print("Six geese a laying, ")
  fifth()
  fourth()
  third()
  second()

def seventh():
  first("seventh")
  print("Seven swans a swimming, ")
  sixth()
  fifth()
  fourth()
  third()
  second()

def eighth():
  first("eighth")
  print("Eight Maids a milking, ")
  seventh()
  sixth()
  fifth()
  fourth()
  third()
  second()

def nineth():
  first("nineth")
  print("Nine Ladies Dancing, ")
  eighth()
  seventh()
  sixth()
  fifth()
  fourth()
  third()
  second()

def tenth():
  first("tenth")
  print("Ten Lords a Leaping, ")
  nineth()
  eighth()
  seventh()
  sixth()
  fifth()
  fourth()
  third()
  second()

def eleventh():
  first("eleventh")
  print("Eleven Pipers Piping, ")
  tenth()
  nineth()
  eighth()
  seventh()
  sixth()
  fifth()
  fourth()
  third()
  second()

def twelfth():
  first("twelfth")
  print("Twelve Drummers Drumming, ")
  eleventh()
  tenth()
  nineth()
  eighth()
  seventh()
  sixth()
  fifth()
  fourth()
  third()
  second()

def print_lyrics():
  first("first")
  pear_tree()
  second()
  pear_tree()
  third()
  pear_tree()
  fourth()
  pear_tree()
  fifth()
  pear_tree()
  sixth()
  pear_tree()
  seventh()
  pear_tree()
  eighth()
  pear_tree()
  nineth()
  pear_tree()
  tenth()
  pear_tree()
  eleventh()
  pear_tree()
  twelfth()
  pear_tree()

print_lyrics()