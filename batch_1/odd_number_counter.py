#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_numbers = 0

for i in range(10):
    user_input = int(input(f"Please input a value {i + 1}: "))      

    if user_input % 2 != 0:
        odd_numbers += 1 

print(odd_numbers)
        
    