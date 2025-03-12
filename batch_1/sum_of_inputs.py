#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
sum_of_inputs = 0

for i in range(10):
    user_input = float(input(f"Please input a number {i + 1}: "))
    sum_of_inputs += user_input

print(sum_of_inputs)



