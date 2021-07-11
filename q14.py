'''
14 Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.
    Note :
    An equilateral triangle is a triangle in which all three sides are equal.
    A scalene triangle is a triangle that has three unequal sides.
    A isosceles triangle is a triangle that has two equal sides.
'''

a=int(input("Enter 1st side:"))
b=int(input("Enter 2nd side:"))
c=int(input("Enter 3rd side:"))
if a==b and a==c:
    print("equilateral triangel")
elif a!=b and b!=c and a!=c:
    print("scalence triangle")
elif a==b or a==c:
    print("isosceles triangle")
else:
    print("invalid")