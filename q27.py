'''
 Write a program to find the sum of the digits of a number accepted from user

'''


n=input("Enter number:")
sum=0
for i in n:
    sum=sum+int(i)
print(sum)