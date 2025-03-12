#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
num_1 = int(input(f"Please input a number: "))
num_2 = int(input(f"Please input a number: "))

if num_1 > num_2:
    print(f"{num_1} is the bigger number.")
else:
    print(f"{num_2} is the bigger number.")