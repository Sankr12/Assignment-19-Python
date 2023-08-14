# Write a python program to create a function to check whether a given number is even or odd.

def even_odd(num):
    if num % 2 == 0:
        print("{} is even number".format(num))
    else:
        print("{} is odd number".format(num))

num = int(input("Enter the number: "))

even_odd(num)