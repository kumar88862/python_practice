#  10 Accept three numbers from the user and display the second largest number.
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

data=[]
data.append(a)
data.append(b)
data.append(c)
data.sort()
print("Second largest Number is:{}".format(data[-2]))