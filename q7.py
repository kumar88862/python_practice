# 7 Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

number=int(input("Enter a number:"))
if number%2==0 and number%3==0:
    print("Yes")
else:
    print("No")