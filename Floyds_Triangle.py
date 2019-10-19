# Write a Program for Floyd’s triangle.
'''
1
2	3
4	5	6
7	8	9	10
11	12	13	14	15
'''
def floyds_triangle(n):
    num = 1
    for i in range(0,n):
        for j in (0,i+1):
            print(num, end=" ")
            num = num + 1
        print('\r')

size = int(input("Enter the size of the Floyd's Triangle: " ))
floyds_triangle(size)