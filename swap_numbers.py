# Write a Program for swapping of two numbers
''' with third variable'''
def swap(a,b):
    print(f'Before Swap: a={a},b={b}')
    temp = a
    a = b
    b = temp
    print(f'After Swap: a={a},b={b}')
swap(1,2)

''' without third variable'''

def swap(a,b):
    print(f'Before Swap: a={a},b={b}')
    a = a + b
    b = a - b
    a = a - b
    print(f'After Swap: a={a},b={b}')
swap(1,2)