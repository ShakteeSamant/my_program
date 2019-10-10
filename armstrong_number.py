# Write a program to check given number is Armstrong number or not.

num = int(input(' Enter the Number:'))
result = 0
power = len(str(num))
temp = num

while (temp!=0) : 
    rem = temp % 10 
    result += rem ** power
    temp = temp // 10  

if num == result :
    print(' Armstrong number')
else:
    print('not an Armstrong number')

#  Armstrong Number using function

def armstrong_numbers(n):
    for i in range(n + 1):
        temp = i
        result=0
        power= len(str(i))
        while (temp!=0) : 
            rem = temp % 10 
            result += rem ** power
            temp = temp // 10  
        if i == result:
            print(i) 

armstrong_numbers(1000)