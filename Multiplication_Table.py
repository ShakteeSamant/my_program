# Write a Program to print Multiplication Table

def mul_table(n):
    for i in range (1, 11):
        print(f'{n} X {i} = {n*i}')

table = input('Enter The Table: ')
table = int(table)
print(f'{table} TABLE')
mul_table(table)
