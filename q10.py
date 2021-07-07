#  10 Accept three numbers from the user and display the second largest number.
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

if a>b and a>c:
    if b>c:
        print("Second largest number is b")
    else:
        print("Second largest number is c")
elif b>a and b>c:
    if a>c:
        print("Second largest number is a")
    else:
        print("Second largest number is c")
else:
    if a>b:
        print("Second largest number is a")
    else:
        print("Second largest number is b")
