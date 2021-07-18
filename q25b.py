'''
 Write a program to display product of the digits of a number accepted from the user.
'''

num=input("Enter number:") #989
l=len(num)
num=int(num)
pro=1  
for i in range(l):
    pro=pro*(num%10)
    num=num//10

print(pro)