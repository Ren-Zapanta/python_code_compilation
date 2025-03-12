#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
#Asks the user for two numeric inputs
num_1 = int(input(f"Please input a number: "))
num_2 = int(input(f"Please input a number: "))
#Checks which input is bigger in value. Prints the bigger one.
if num_1 > num_2:
    print(f"{num_1} is the bigger number.")
else:
    print(f"{num_2} is the bigger number.")