# Write a Program to find largest among three numbers using binary minus operator.

def largest_num(a,b,c):
    if ((a>b)and (a>c)):
        print('Largest number is ',a)
    else:
        if ((b>c)):
            print('Largest number is ',b)
        else:
            print('Largest number is ',c)
largest_num(10,15,20)