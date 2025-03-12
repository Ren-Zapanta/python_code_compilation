#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
#Asks the user for 2 inputs
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))
#Use modulus operator to obtain remainder
get_remainder = num_1 % num_2
#Print result
print(get_remainder)


