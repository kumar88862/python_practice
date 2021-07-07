'''
8 Accept the following from the user and calculate the percentage of class attended:
   Total number of working days
   Total number of days for absent
'''
total_number_of_working_days=int(input(" Total number of working days:"))
total_number_of_days_for_absent=int(input(" Total number of days for absent:"))
total_number_of_days_for_present=total_number_of_working_days-total_number_of_days_for_absent
percentage=round((total_number_of_days_for_present/total_number_of_working_days)*100,3)

print("Percentage:"+str(percentage))
print("Percentage:{}".format(percentage))