#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
#Initiatlize list
numbers_list = 0 
#Loop to request 10 entries from the user
for i in range(10):
    user_input = int(input(f"Please enter a value {i + 1}: "))
    #Append user entries to the empty list
    numbers_list.append(user_input)