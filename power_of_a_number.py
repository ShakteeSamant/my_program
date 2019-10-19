# Write a Program to find out power of number. 

def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power

square = to_power(2)
cube = to_power(3)

print(square(9))
print(cube(9))