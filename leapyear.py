#Bhaveesh Beemireddy CS362 HW#1
#run program and enter the year you want to calcuate for output
x= int(input("enter year:")) #take in user inut for leap year calucation
if (x<0):                #Now check if user input is a positive number
    print("Enter a postive number, program has quit")
                      
elif (x % 4== 0) and (x % 100 != 0): #conditions for leap year updated
    print(x, "is a leap year")

elif (x % 400 == 0):
    print(x, "is a leap year")

else:
    print(x, "is not a leap year")
