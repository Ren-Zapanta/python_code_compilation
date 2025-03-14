#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
#Initialize empty list for user entries
input_list = []
#Asks the user for 10 numeric entries
for i in range(10):
    user_input = int(input(f"Please input a value ({i + 1}): "))
    input_list.append(user_input)
#Initialize list for unique inputs
unique_input = [user_input for user_input in input_list if input_list.count(user_input) == 1]
#print result
print(unique_input)
