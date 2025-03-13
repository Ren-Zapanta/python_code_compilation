#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
#Initialize list for duplicates
duplicate_list = []
#Loop that stops if input is invalid
while True:

    #Requests inputs from the user
    user_input = input("Please enter a value: ")
    #Verifies if user input is valid
    if not user_input.isdigit():
        break

    #appends converted user input
    duplicate_list.append(int(user_input))

