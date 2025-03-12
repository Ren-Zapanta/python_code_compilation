#Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
num1 = int(input(f"Please input a number: "))
num2 = int(input(f"Please input a number: "))

if num1 > num2:
    print(f"{num1} is the bigger number.")
else:
    print(f"{num2} is the bigger number.")