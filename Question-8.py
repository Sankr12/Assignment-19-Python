# Write a python program to multiply all the numbers in a list 

def multiplyy(l1 = []):
    result = 1
    for i in l1:
        result*=i
    print("The multiplication of all elements of {} = {}".format(l1,result))

num = int(input("How many numbers you want to do their sum: "))
li = []
for i in range(num):
    num_input = int(input("Enter number {}: ".format(i+1)))
    li.append(num_input)

multiplyy(li)