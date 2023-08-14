# Write a python program to create a function to check whether a number falls in a given range

def check(b,a,c):
    if b in range(a,c):
        return True
    else:
        return False

Range = input("Do you want to set range if no then it will be default as natural number upto 100")
if Range == "Yes" or Range == "yes":
    initial = int(input("Enter the initial range: "))
    final = int(input("Enter the final range: "))
else:
    initial = 1
    final = 101

num = int(input("Enter the number: "))

resutl = check(num,initial,final)
print(resutl)