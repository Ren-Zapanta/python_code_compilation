#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
#Initialize numbers list
numbers_list = []
#Use for loop to request 10 entries from user
for i in range(10):
    user_input = int(input(f"Please enter a number {i + 1}: "))
    numbers_list.append(user_input) #append use_inputs to numbers_list


