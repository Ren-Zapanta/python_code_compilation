#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
#Use for loop to iterate nunmbers
for i in range(101):
    #Check if a number is divisible by zero
    if i % 10 != 0:
        #Omit numbers divisible/ending in zero
        print(i)