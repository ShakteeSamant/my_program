# wether the number is perfet number or not??????

num = int(input("Enter the number : "))
result = 0
for i in range(1,num):
    if num % i == 0:
        result += i

if result == num:
    print(f'{num} is a Perfect number')
else:
    print(f'{num}  is not a Perfect number')


# Print the Perfect numbers 

nums = int(input('Enter the range : '))
result =  0
for num in range (1, nums+1):
    for i in range(1,num):
        if num % i == 0:
            result += i

    if num == result:
        print (num)
    result = 0

