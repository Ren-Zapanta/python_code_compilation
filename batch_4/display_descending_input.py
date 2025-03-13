#Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
#Initialized empty list
number_list = []

#Loop to request input from user
while True:
    #Requests entries from user
    user_input = input("Please enter a value: ")
    #stops the loop if input is invalid
    if not user_input.isdigit():
        break
    #Converts data type
    user_input = int(user_input)
     #appends user input to number list
    number_list.append(user_input)
    #use sort function to sort elments inside list
    number_list.sort(reverse=True)
#print sorted list
print(number_list)

    