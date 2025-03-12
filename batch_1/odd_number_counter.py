#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_numbers = 0
#Use for loop to iterate prompt requesting 10 inputs
for i in range(10):
    user_input = int(input(f"Please input a value {i + 1}: "))      
    #Check if remainder is not equal to zero, then odd
    if user_input % 2 != 0:
        #if odd, then increase by 1
        odd_numbers += 1 
#print odd numbers
print(odd_numbers)
        
    