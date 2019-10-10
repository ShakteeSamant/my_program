# Write a program to check given number is palindrome number or not.

num = input('Enter a number')
rev = num[::-1]

if num == rev:
    print (num, 'palindrome number')
else:
    print(num, 'Not palindrome')