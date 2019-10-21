# Write a Program to count number of digits in a number

n = 1234567890
digits = len(str(n))
print(digits)


'''----------------------------------------'''

num = int(input('Enter the Number : '))
count = 0
while(num!=0):
    
    count += 1
    num=num//10

print('number of digits =',count)
    