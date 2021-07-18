'''
 Write a program to display product of the digits of a number accepted from the user.
'''

n=input("Enter number to get product of digits:") #123
pro=1 
for i in n:
    pro=pro*int(i)
print(pro)
    