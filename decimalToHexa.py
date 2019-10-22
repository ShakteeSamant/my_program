# Write a Program to convert decimal number to  hexadecimal number.


def decimalToHexa(n):
    hexa_code= {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    if(n > 15): 
        decimalToHexa(n//16)  
    rem = n % 16
    if rem >=10 :
        print(hexa_code[rem], end=' ')
    else:
        print(rem, end=' ')




# Write a Program to convert hexadecimal number to  decimal number.

def hexaToDecimal(hexa): 
    hexa_code= {'0':0,'1': 1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    decimal, i= 0, len(hexa)-1
    if hexa !=0 :
        for hex in hexa:
            decimal = decimal + hexa_code[hex] * pow(16,i)
            i -= 1
    print(decimal)   

hex = input('\nEnter the HEXA Value: ')


if __name__ == "__main__":
    decimalToHexa(313565)

    hexaToDecimal(hex) 
    