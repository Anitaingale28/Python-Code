# Program to find the largest of two numbers

def find_largest(num1, num2):
    if num1 > num2:
        print(f"The largest number is {num1}")
    else:
        print(f"The Smallest number is {num2}")

# Taking user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function
find_largest(num1, num2)
