# Write a python program to create a function which expects a list as an argument.

def fruits(fru=[]):
    for i in fru:
        print(i)

fruit = ["Apple", "Mango", "Banana", "Pineapple", "Watermelon"]
fruits(fruit)