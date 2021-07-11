'''
13  Accept the age, gender (‘M’, ‘F’), number of days and display the wages accordingly

     Age	Sex	Wage/day
     >=18 and <30	M	700
                    F	750
     >=30 and <=40	M	800
                    F	850
'''

age = int(input("Enter age :"))
gender=input("Enter gender :").upper()
days=int(input("Enter number of days :"))

if age>=18 and age<30 and gender=='M':
    print("Total amount:"+str(days*700))
elif age>=18 and age<30 and gender=='F':
    print("Total amount:"+str(days*750))
elif age>=30 and age<=40 and gender=='M':
    print("Total amount:"+str(days*800))
elif age>=30 and age<=40 and gender=='F':
    print("Total amount:"+str(days*850))
else:
    print("Invalid input")

