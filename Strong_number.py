# Write a program to check given number is strong number or not

num = int(input(" Enter the number: "))
temp = num
result = 0
def fact(n):
    if n == 1:
       return n
    else:
       return n*fact(n-1)

for i in range(len(str(num))):
    digit = temp % 10
    result = result + fact(digit)
    temp= temp//10

if num == result:
    print('Strong number')
else:
    print('not a Strong Number')