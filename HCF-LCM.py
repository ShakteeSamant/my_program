# Python program to find GCD and LCM of two numbers 
  
def hcf(a,b): 
    if a == 0: 
        return b 
    return hcf(b % a, a)

def lcm(a,b): 
    return (a*b) / hcf(a,b) 

a = 13
b = 123
print('LCM of', a, 'and', b, 'is', lcm(a, b)) 
print('HCF of', a, 'and', b, 'is', hcf(a, b))

''''----------------GCD or HCF ----------------------------------------------'''

def gcd(a,b): 

    if (a == 0): 
        return b 
    if (b == 0): 
        return a
    if (a == b): 
        return a 
   
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a) 

a = 98
b = 56
if (gcd(a, b)): 
    print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
else: 
    print('not found') 