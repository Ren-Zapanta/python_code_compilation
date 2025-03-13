#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
#Initialize empty lists
numbers_list = [] 
duplicates_list = []  

#Requests 10 inputs from the user
for i in range(10):
    user_input = int(input(f"Please enter a number {i + 1}: "))  
    numbers_list.append(user_input)

