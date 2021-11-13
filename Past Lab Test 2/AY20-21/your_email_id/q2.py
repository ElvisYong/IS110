# Name:
# Email ID:
def get_hi_lo(products):

    # Write your code here.
    if products:
        hi_product = ''
        high = 0
        low_product = ''
        low = 0

        for product in products:
            name, price = product
            if price > high:
                high = price
                hi_product = name
            if low < price:
                low = price
                low_product = name

        return (hi_product, low_product)
        
    return (None, None)

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)
    
    products = [('apple', 100), ('orange', 200), ('pear', 300)]
    print(f"Test Case {tc_num} : get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : ('pear', 'apple')")
    print(f"Actual   : {result}")
    print()
    
    print("Expected return type : <class 'tuple'>")
    print(f"Actual return type   : {type(result)}")    
    
    print()
    
    print("Expected return type of the first element of the tuple : <class 'str'>")
    print("Actual return type of the first element of the tuple   : ", end="")
    if (isinstance(result, tuple)):
        print(type(result[0]))
    else:
        print("N/A")

    tc_num += 1
    print('-' * 40)
    
    products = [('apple',100),('orange',250),('pear',200),('banana',150)]
    print(f"Test Case {tc_num} : get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : ('orange', 'apple')")
    print(f"Actual   : {result}")
    print()

    tc_num += 1
    print('-' * 40)
    
    products = [('apple', 100)]
    print(f"Test Case {tc_num} : get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : ('apple', 'apple')")
    print(f"Actual   : {result}")
    print()

    tc_num += 1
    print('-' * 40)
    
    products = []
    print(f"Test Case {tc_num}:get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : (None, None)")
    print(f"Actual   : {result}")
    print()
