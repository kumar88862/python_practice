# 3 Write a program to check whether a number (accepted from user) is positive or negative.
number=input("Enter a number:").strip()
if number[0]=='-':
    print("Negative")
else:
    print("Positive")