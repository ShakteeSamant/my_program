# Write a Program to get factorial of given number.
'''Using While Loop'''

def factorial(n):
    num = n
    fact=1
    while n!=0:
        fact=fact*n
        n= n-1
    return f'{num}!= {fact}'

print(factorial(6))


''' Using For Loop'''

def factorial(n):
    num = n
    fact=1
    for i in range(n,0,-1):
        fact = fact * i
    return f'{num}!= {fact}'

print(factorial(25))

''' Using recursion method'''

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(0))