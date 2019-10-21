# Write a Program to convert decimal number to binary number.

def decimalToBinary(n):
    if(n > 1): 
        decimalToBinary(n//2)  
    print(n%2, end=' ')

decimalToBinary(235)


# Write a Program to convert binary number to decimal number.

def binaryToDecimal(binary): 
 
    decimal, i= 0, 0
    while(binary != 0): 
        bit = binary % 10
        decimal = decimal + bit * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)     

binaryToDecimal(100) 