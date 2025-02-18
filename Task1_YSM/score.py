# Program to find grade

def grade(score):
    if 90 <= score <=100:
        print(f"Grade A")
    elif 80<= score <90:
        print(f"Grade B")
    elif 70<= score <80:
        print(f"Grade C")
    elif 60<= score <70:
        print(f"Grade D")
    elif 50<= score <60:
        print(f"Grade E")
    elif 40<= score <50:
        print(f"Grade F")
    else:
        print(f"Fail")



# Taking user input
score= float(input("Enter the score number: "))


# Calling the function
grade(score)
