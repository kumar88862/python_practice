'''
Write a program to print table of a number accepted from user.
'''

n =int(input("Enter a number:")) #10

for i in range(1,11):
    print('{} * {}  = {}'.format(n,i,n*i))