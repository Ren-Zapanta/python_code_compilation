#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.
#Initiatlize list
numbers_list = 0 
#Loop to request 10 entries from the user
for i in range(10):
    user_input = int(input(f"Please enter a value {i + 1}: "))
    #Append user entries to the empty list
    numbers_list.append(user_input)
    #Initialize counter for even numbers
even_count = 0
#Iterate through each value stored in numbers_list
for user_input in numbers_list:
    #Checks if number is even
    if user_input % 2 == 0:
        #adds to the even_count
        even_count += 1
#Prints even numbers inputed 
print(even_count)
