# Program to check first number is grtater ,smaller,equal to second number

def num_check(num1, num2):
    if num1 > num2 :
        print(f"The {num1} is grater than {num2}")
    elif num1 < num2:
        print(f"The {num1} is smaller than {num2}")
    else:
        print(f"The {num1} is equal to {num2}")
    

# Taking user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function
num_check(num1, num2)
