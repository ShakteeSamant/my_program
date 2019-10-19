# Write a Program to find out sum of digit of given number.

def digit_sum(n):
    sum_ = 0
    for i in range(len(str(n))):
        digit = n % 10 
        sum_ += digit
        n = n//10
    return sum_

num = int(input('Enter the num : '))
print(digit_sum(num))
