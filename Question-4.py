# Write a python script to create a function which expects kwargs arguments.

def fruits_seller(**fruits):
    for key, value in fruits.items():
        print("Your {} is {}".format(key,value))

fruits_seller(Mango = "Sour", Apple = "Fresh", Tomato = "Expensive", Banana = "Rotted")