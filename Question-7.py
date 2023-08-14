# Write a python program to sum all the numbers in a list.

def addition(li=[]):
    result = sum(li)
    print("The sum of all elements of {} = {}".format(li,result))

num = int(input("How many numbers you want to do their sum: "))
l1 = []
for i in range(num):
    num_input = int(input("Enter number {}: ".format(i+1)))
    l1.append(num_input)

addition(l1)