#5 Write a program to check whether an years is leap year or not.

year=int(input("Enter Year:"))
if year%100==0:
    if year%400==0:
        print("leap year")
    else:
        print("not leap year")
    
else:
   if year%4==0:
       print("leap year")
   else:
        print("not leap year")