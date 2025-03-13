#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
#Initialize total and count variables and set them to 0
numbers_total = 0
count_total = 0

while True: #Requests input from the user
    user_input = input("Please enter a value: ")

    if not user_input.isdigit(): #Verifies input validity
        break #Breaks loop if invalid input

    user_input = int(user_input) #Convert user_input to int datatype
    numbers_total += user_input #Adds the user input to the numbers_total variable
    count_total += 1 #Increase count of input

if count_total > 0: #Verifies if there is at least one input
    input_average = numbers_total / count_total #Calculates the average
    print(input_average) #Prints calculated average
else: 
    ("Nothing entered") #Prints if nothing no input