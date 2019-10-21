# Write a Program to find out prime factor of given number.


def factors(n):
    num=[]
    for i in range(1,n):
        if n%i == 0:
            num.append(i)
    return num

num= int(input('Enter the Number: '))
print(factors(num))