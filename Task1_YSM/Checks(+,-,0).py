# Program to check  the  positive ,neghative,and zero

def Check(num):
    if num > 0:
        print(f"The {num} is positive number")
    elif num < 0:
        print(f"The {num} is negative number")
    else:
        print(f"The {num} is zero")
    

# Taking user input
num = float(input("Enter the  number: "))


# Calling the function
Check(num)
