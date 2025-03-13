#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
#Initialize total and count variables and set them to 0
numbers_total = 0
count_total = 0

while True: #Requests input from the user
    user_input = input("Please enter a value: ")

    if not user_input.isdigit(): #Verifies input validity
        break #Breaks loop if invalid input

 