'''
Write code for checking whether a given year is leap year or not.

Input Format

The year for which the leap year has to be found should be given as input. eg. 2017

Constraints

Only year has to be given.
'''
year=int(input())
if year%400==0:
    print("Leap Year")
elif year%100==0:
    print("Not Leap Year")
elif year%4==0:
    print("Leap Year")
else:
    print("Not Leap Year")