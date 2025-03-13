#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
#Initialized empty list
input_list = []

#Loop that runs indefinitley unless invalid input
while True:

    #Requests inputs from the user using loop
    user_input = input("Please enter a value: ")
    #Checks if user input is valid
    if not user_input.isdigit():
        break

    #Cnverts data type
    user_input = int(user_input)