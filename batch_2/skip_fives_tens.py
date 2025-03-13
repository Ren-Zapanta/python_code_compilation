#Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
#loop through numbers 0 to 100
for i in range(101):
    if i % 5 != 0 and i % 10 != 0: #checks if numbers are not divisible by either 5 or 10
        #print result
        print(i)