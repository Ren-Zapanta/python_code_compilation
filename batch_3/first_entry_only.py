#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
#Initialize list for entries
input_list = []
#Requests 10 inputs from the user
for i in range(10):
    user_input = int(input(f"Please enter a number {i + 1}: "))
    #verifies if input is already on the list
    if user_input not in input_list:
        #appends input if not yet on the list
        input_list.append(user_input)
#Print final list
print(input_list)
