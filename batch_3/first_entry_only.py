#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
#Initialize list for entries
input_list = []

for i in range(10):
    user_input = int(input(f"Please enter a number {i + 1}: "))