# Write a python program to create a function that finds a maximum of four arguments

def maximum_value(L1=[]):
    result = max(L1)
    return result

lis = []
for i in range(4):
    a = int(input("Enter the number {}: ".format(i+1)))
    lis.append(a)

last = maximum_value(lis)
print(last)