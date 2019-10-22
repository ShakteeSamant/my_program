# Write a Program to convert binary number to octal number.

import decimalToBinary
import decimalToOctal

binary = int(input('Enter the Binary Value: '))
decimal = decimalToBinary.binaryToDecimal(binary)
# decimal= decimal.strip()
decimal= int(decimal)

octal = decimalToOctal.decimalToOctal(decimal)

print(f'Binary {binary} = {octal}')