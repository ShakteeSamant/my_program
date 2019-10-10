# Write a program to check given string is palindrome or not.

string = input('Enter a word :').lower()
rev_str = string[::-1]

if string == rev_str:
    print (string, 'is Palindrome ')
else:
    print(string, 'Not palindrome')