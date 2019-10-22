# Write a Program to convert decimal number to Octal number.

def decimalToOctal(n):
    if(n > 7): 
        decimalToOctal(n//8)  
    print(n%8,end='')



# Write a Program to convert Octal number to decimal number.

def octalToDecimal(octal): 
    temp,decimal, i= octal,0, 0
    while(octal != 0): 
        bit = octal % 10
        if bit < 7:
            decimal = decimal + bit * pow(8, i) 
            octal = octal//10
            i += 1
        else:
            print('\nEnter valid Octal number')
            break
    print('\n')
    print('Decimal Value of',temp,'=', decimal)    




if __name__ == "__main__":
    
    decimalToOctal(98)


    octalToDecimal(142)
