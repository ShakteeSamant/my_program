# Write a Program to add two numbers without using addition operator.

def add(a,b):
    return a+b
print(add(3,5))

print(2+3)

a= 5
b= 6
print(a+b)


# # Addition of two numbers without using '+' Operator

def Add(x, y): 
  
    while (y != 0): 
        carry = x & y 
        x = x ^ y 
        y = carry << 1
    return x 
  
print(Add(150, 132)) 