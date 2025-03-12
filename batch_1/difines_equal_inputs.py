#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
#Asks the user for two numeric inputs
num_1 = int(input(f"Please input a number: "))
num_2 = int(input(f"Please input another number: "))
#Verifies if both inputs are equal in value
if num_1 == num_2:
    print("Equal")
#Prints equal if values are equal. Prints not equal if otherwise
else:
    print("Not equal")
