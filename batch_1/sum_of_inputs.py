#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
#Initialize sum variable
sum_of_inputs = 0
#use for loop to iterate a prompt asking for 10 inputs
for i in range(10):
    user_input = float(input(f"Please input a number {i + 1}: "))
    #add all input to sum variable
    sum_of_inputs += user_input
#print result
print(sum_of_inputs)



