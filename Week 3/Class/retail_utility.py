def calculate_max_quantity_and_change(unit_price, amount):
    maximum_quantity = amount // unit_price
    change = amount % unit_price
    return (maximum_quantity, change)
  
