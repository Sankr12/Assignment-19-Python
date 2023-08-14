'''Write a python program to create a function which expects two arguments and print 
it in function body'''

def func(args1,args2):
    print("First argument:",args1)
    print("Second argument:",args2)
    return args1,args2

arg1_input = input("Enter the first argument: ")
arg2_input = input("Enter the second argument: ")

result = func(arg1_input,arg2_input)
print("Result value:",arg1_input,arg2_input)