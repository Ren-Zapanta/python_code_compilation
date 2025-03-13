#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
#Initialized empty list
lowest_value = None

#Loop that runs indefinitley unless invalid input
while True:

    #Requests inputs from the user using loop
    user_input = input("Please enter a value: ")
    #stops the loop if input is invalid
    if not user_input.isdigit():
        break

    #Converts data type
    user_input = int(user_input)
    #verify is first input is None. Then, verify if succeeding inputs are less than current lowest.
    if lowest_value is None or user_input < lowest_value:
        #update lowest number
        lowest_value = user_input
#print result
print(lowest_value)