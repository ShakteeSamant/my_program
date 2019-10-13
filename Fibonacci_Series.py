# Write a Program to print Fibonacci series of given range

def fibonacci_numbers(n):
    a=0
    b=1
    if n<0:
        print('Invalid Input')
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c=a+b
            a=b
            b=c
            print(c)

fibonacci_numbers(10)


# Python Program for n-th Fibonacci number

def fib(n):
    a=0
    b=1
    if n <= 0:
        return 'Invalid Input'
    if n == 1:
        return a
    else:
        for i in range(2, n):
            c=a+b
            a=b
            b=c
        return c

print(fib(10))
