#Introduction.
print("\nThis Is Sum Calculator Using Loop.")
print("\t Lets Test It!!")

#Taking A Number As Input From User and Storing In Variables Named as "Num_1".
Num_1=int(input("\nEnter a Number: "))
i=0
a=0

#Using Loop With Main Logic.
while i<= Num_1:
    a=a+i 
    print(a)
    i=i+1 #Increment By One.

#Printing The Total Sum.
print(f"So, Total Sum Of Your Entered Number: {a}")

#Program End.
