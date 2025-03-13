#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
#initialize empty list
input_list = []
#Loop that runs indefinitley unless invalid input

while True:

    #Requests inputs from the user
    user_input = input("Please enter a value: ")
    #Verifies if user input is valid
    if not user_input.isdigit():
        break

    #Cnverts data type
    user_input = int(user_input)

        #Verifies if input is already in list or not 
    if user_input in input_list:
        print("Duplicate") #Prints if duplicate input
    else:
        print("Unique") #Prints if input is unique
        input_list.append(user_input) #adds new user input to list
    