#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
num_1 = int(input(f"Please input a number: "))
num_2 = int(input(f"Please input a number to raise the first input to: "))

exponentiate = num_1 ** num_2

print(exponentiate)