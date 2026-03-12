#Introduction
print("\nThis Is Largest Number Checker Made by Using Python.")
print("\t\tLets Test It!!")

#Taking Three Number As Input From User and Storing In Variables Named as "Num_1","Num_2" And "Num_3".
Num_1=float(input("\nEnter First Number: "))
Num_2=float(input("\nEnter Second Number: "))
Num_3=float(input("\nEnter Third Number: "))
largest=0
#Using If-Else Ladder To check Biggest Number.
if Num_1>Num_2 and Num_1>Num_3:
    largest=Num_1
elif Num_2>Num_1 and Num_2>Num_3:
    largest=Num_2
elif Num_3>Num_1 and Num_3>Num_2:
    largest=Num_3

#Using fstring To Print Largest Number.  
print(f"Largest Number is {largest}")

#Program End And \t for Tab And \n For New Line
print("\n\t\t\tThankyou!!")