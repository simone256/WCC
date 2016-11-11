#def multiply(a, b):
#    result = a * b
#    return result

#solution = multiply(4, 5) # Invoke multiply giving it the arguments 4 and 5
#print(solution) # Expected: 20

#def mystery(x, y, z):

    # ??? Your code here
#    result = x + y * z
#    return result

#print mystery('Hello', 3, '!') # Expected: 'Hello!!!'
#print mystery('Goodbye', 2, '@') # Expected: 'Goodbye@@'


def calculate_tip(price, rating):
    if rating == 'A':
        tip = .20;
    elif rating == 'B':
        tip = .18;
    else:
        tip = .15;

    amount = price * tip;
    return amount


print(calculate_tip(30.50, 'C')) # Expected: 4.575
print(calculate_tip(15.00, 'B')) # Expected: 2.7
print(calculate_tip(20.00, 'A')) # Expected: 4
