#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
#Asks the user for 2 inputs
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter a number: "))
#Check which input is smaller 
if num_1 > num_2:
    print(f"{num_2} is smaller")
else:
    print(f"{num_1} is smaller")

