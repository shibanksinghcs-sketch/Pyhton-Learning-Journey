#Introduction
print("This Is An Calculator Made by Using Python.")
print("\t\tLets Test It!!")

#Taking First and Second Number As Input From User and Storing In Variables Named as "Num_1" & "Num_2".
num_1=int(input("Enter First Number: "))
num_2=int(input("Enter Second Number: "))

# Performing and Printing Addition, Subtraction, Multiplication and Divison of Both The Inputs Using fstring Function. 
print(f'\nAddition of First & Second Number is "{num_1+num_2}".')
print(f'Subtraction of First & Second Number is "{num_1-num_2}".')
print(f'Multiplication of First & Second Number is "{num_1*num_2}".')

#Denomerator Can't Be 0 in Division, Because Not Defined in Mathematical Term Universally.
if num_2==0:
    print("Divisor(2nd Number) Should'nt be Zero. Try Again!!")
else:
    print(f'Division of First & Second Number is "{num_1/num_2}".')

#Program End And \t for Tab And \n For New Line.
print("\t\n\t\tThankyou!!")
