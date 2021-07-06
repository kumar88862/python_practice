# 4 Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.

number=input("Enter a number:").strip()
if int(number[-1])%3==0:
    print("Divisible")
else:
    print("Not Divisible")