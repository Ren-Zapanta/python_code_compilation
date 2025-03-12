#Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
#Request 2 inputs from the user
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))
#Perform floor division on the inputs
get_quotient = num_1 // num_2
#Print the result without decimal
print(get_quotient)