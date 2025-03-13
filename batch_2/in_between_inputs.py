#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
#requests 2 inoputs from the user
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter another number: "))
#Determines the range using the two inputs
ceil_input = max(num_1, num_2)
floor_input = min(num_1, num_2)
for i in range(floor_input + 1, ceil_input):
    print(i)