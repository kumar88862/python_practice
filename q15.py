'''
15  Write a program to accept percentage and display the Category according to the  following criteria :
    Percentage	Category
    < 40	Failed
    >=40 & <55	Fair
    >=55 & <65	Good
    >=65	Excellent
'''


percentage=int(input("Enter the percentage:"))
if percentage<40:
     print("Failed")
elif percentage>=40 and percentage<55:
     print("Fair")
elif percentage>=55 and percentage<65:
     print("Good")
elif percentage>=65 and percentage<=100:
     print("Excellent")
else:
    print("Please enter correct percentage")