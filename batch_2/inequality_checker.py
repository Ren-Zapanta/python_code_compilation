#Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
#Asks the user for 2 inputs
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))
#Verify if inputs are equal or not
if num_1 == num_2:
    print("Equal")#Print equal if inputs are equal
else:
    print("Not Equal")#Print not equal if inputs are not equal