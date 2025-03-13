#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
#Initialized empty list
number_list = []

#Running loop unless invalid input is entered
while True:

    #Requests entries from user
    user_input = input("Please enter a value: ")
    #stops the loop if input is invalid
    if not user_input.isdigit():
        break
    #Converts data type
    user_input = int(user_input)




