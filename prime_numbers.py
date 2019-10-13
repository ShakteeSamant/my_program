# Write a program to check given number is prime number or not.

num = int(input('Enter the number: '))
count = 0
for i in range(2,num+1):
    if num % i == 0:
        count += 1
if count == 1:
    print ('Prime number')
else:
    print('Not Prime')



# prime numbers between the range of 100 numbers

for num in range(101):
    count = 0
    for i in range(2,num+1):
        if num % i == 0:
            count += 1
    if count == 1:
        print (i)


# WAP to find prime numbers between two numbers.

def prime(l, u):
    for num in range(l, u+1):
        count = 0
        for i in range(2,num+1):
            if num % i == 0:
                count += 1
        if count == 1:
            print (num)

low = int(input('Enter the lower number: '))
upp = int(input('Enter the upper number: '))
prime(low,upp)

