#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
#Initialize empty lists
numbers_list = [] 
duplicates_list = []  

#Requests 10 inputs from the user
for i in range(10):
    user_input = int(input(f"Please enter a number {i + 1}: "))  
    #append user input to numbers list
    numbers_list.append(user_input)

for user_input in numbers_list: 
    if numbers_list.count(user_input) > 1 and user_input not in duplicates_list: #Verifies if input is a duplicate or not
        duplicates_list.append(user_input) #appends input to duplicates list

print(duplicates_list)
