"""
 Accept the percentage from the user and display the  grade according to the following criteria:

    Below 25 —- D
    25 to 45 —- C
    45 to 50 —- B
    50 to 60 –– B+
    60 to 80 — A
    Above 80 –- A+
"""

percentage=int(input("Enter percentage:"))

if percentage>=80:
    print("A+")
elif percentage>=60 and percentage<80:
    print("A")
elif percentage>=50 and percentage<60:
    print("B+")
elif percentage>=45 and percentage<50:
    print("B")
elif percentage>=25 and percentage<45:
    print("C")
else:
    print("D")
