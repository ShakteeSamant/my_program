# Write a Program to subtract two numbers without using subtraction operator.

def sub(a,b):
    return a-b
print(sub(3,5))

print(5-3)

a= 50
b= 6
print(a-b)

def subtract(x, y): 
    while (y!=0):
        borrow = (~x & y)
        x = x ^ y
        y = borrow << 1
    return x    


x = 29
y = 13
print(f"{x} - {y} =", subtract(x, y))

