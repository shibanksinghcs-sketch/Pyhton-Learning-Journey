#Introduction
print("\nThis Is An Grade Checker!! Checks Grade on basis of Percentage Made by Using Python.")
print("\t\t\t\tLets Test It!!")

#Taking Percentage As Input From User and Storing In Variables Named as "Percentage".
Percentage=float(input("\nEnter The Percentage: "))

# Using If-Else Ladder For Checking Grade According To Percentage.
if Percentage>=90:
    print("Grade-A, Exellent!!")
elif Percentage<90 and Percentage>=80:
    print("Grade-B,Very Good!!")
elif Percentage<80 and Percentage>=70:
    print("Grade-C, Good!!")
elif Percentage<70 and Percentage>=60:
    print("Grade-D, Need Improvement!!")
elif Percentage<60 and Percentage>=40:
    print("Grade-E, Below Average.")
elif Percentage<40 and Percentage>=0:
    print("Grade-F, Poor Result.")
else:
    print("Enter Valid Percentage Between(0-100).")

#Program End And \t for Tab And \n For New Line
print("\n \t \t \t \t Thankyou!!")