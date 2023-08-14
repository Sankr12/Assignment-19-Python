# Write a python program to create a function which expects an unknown number of arguments 

print()
def unknown_args(*t):
    Avg = sum(t)/len(t)
    return Avg

num = int(input("Enter the numbers to get the average of: "))
a = []
for i in range(num):
    in_put = int(input("Enter the {} number: ".format(i+1)))
    a.append(in_put)

result = unknown_args(*a)
print("Average of your given numbers:",result)