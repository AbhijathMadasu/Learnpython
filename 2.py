x = float(input("Enter first number: " ))
y = float(input("Enter second number: "))
def diff(x, y):
    if x > y:
        subtract = x - y
    else:
        subtract = y - x
    return subtract
print("The difference between numbers = ", diff(x, y) )
