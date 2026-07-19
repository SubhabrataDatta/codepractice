#Code to Calculate your age in (i) Year month and days; and (ii) total days
#You need to first install python-dateutil by using command
#pip install python-dateutil

#Concepts explored in this practice
#1. f"..." is an f-string (formatted string literal). The f tells Python: "look inside this string for {...} 
#and replace them with the value of the code inside."
#2. pip install and import
#3. dateutil and relative data


from datetime import date
from dateutil.relativedelta import relativedelta

year=int(input("What's your year of birth ? \n: "))
month=int(input("What's your month of birth (Answer in 1-12)? \n: "))
day=int(input("What's your day of birth (Answer in 1-31)? \n: "))
birthdate=date(year,month,day)
print("\n\n\n\nYou were born on " + str(birthdate))

today=date.today()

#relativedelta handles calendar math
delta=relativedelta(today,birthdate)

print(f"\n\n\n\nToday you are {delta.years} years {delta.months} months {delta.days} days" )

#for total number of months
monthx=12*delta.years
months=monthx+delta.months
print(f"\n\n\n\nOr we can also you are {months} months old")

#for total number of days
age_days=(today-birthdate).days
print(f"\n\n\n\nOr we can also you are " + str(age_days) + "days old\n")