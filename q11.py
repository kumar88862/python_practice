'''
11 A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
    Ask user for their salary and year of service and print the net bonus amount.
'''
salary=int(input("Enter salary:"))
exp=int(input("Experience:"))

if exp>=5:
    net_bonus=1/100*salary*5
    print("Net Bonus={}".format(net_bonus))
else:
    print("Net Bonus=0")



