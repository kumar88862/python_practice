# 6 Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

input=input("Enter a number:").strip()
if input=="1":
    print("Sunday")
elif input=="2":
    print("Monday")
elif input=="3":
    print("Tuesday")
elif input=="4":
    print("Wednesday")
elif input=="5":
    print("Thursday")
elif input=="6":
    print("Friday")
elif input=="7":
    print("Saturday")
else:
    print("Invald input")