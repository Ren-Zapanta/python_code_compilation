#Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
#Sets an initial variable as None
highest_value = None

while True: #Loop to request entries from user
    user_input = input("Please enter a number: ")

    if not user_input.isdigit(): #Stops loop if input is invalid
        break

    user_input = int(user_input) #converts user_input into int data type

    if highest_value is None or user_input > highest_value: #Verifies if the current input is the highest one
        highest_value = user_input
#Verifies if at elast one number is inputted
if highest_value is not None:
    print(highest_value) #Prints the highest value input
else:
    print("Nothing Entered")#Prints if no input


