#!/usr/bin/env python
# coding: utf-8

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
"Saturday", "Sunday"]

months = ["January", "February", "March", "April", "May", "June",\
"July", "August", "September", "October", "November", "December"]

days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
starting_year = 1901
starting_day = 1
starting_days = 1
starting_month = "January"
starting_date = str(starting_day) + "/" +\
str(months.index(starting_month) + 1) + "/" + str(starting_year)
ending_year = 2000
ending_day = 31
ending_month = "December"
ending_date = str(ending_day) + "/" + str(months.index(ending_month) + 1) +\
"/" + str(ending_year)
counter = 0

while starting_date != ending_date:	
    if days[starting_days] == "Sunday":
        if starting_day == 1:
            counter += 1
            print str(counter) + "-->" + starting_date 
        starting_days = 0	
    else:
        starting_days += 1

    if starting_year % 4 != 0 or (starting_year % 100 == 0 and starting_year % 400 != 0):
        if starting_month == "December" and starting_day == 31:
            starting_month = "January"
            starting_day = 1
            starting_year += 1
        elif starting_day == days_of_month[months.index(starting_month)]:
            starting_month = months[months.index(starting_month) + 1]
            starting_day = 1
        else:
            starting_day += 1

    elif starting_year % 4 == 0:
        if starting_month == "February" and starting_day == 29:
            starting_month = "March"
            starting_day = 1
        elif starting_month == "December" and starting_day == 31:
            starting_month = "January"
            starting_day = 1
            starting_year += 1
        elif starting_day == days_of_month[months.index(starting_month)] and starting_month != "February":
            starting_month = months[months.index(starting_month) + 1]
            starting_day = 1
        else:
            starting_day += 1

    starting_date = str(starting_day) + "/" +\
str(months.index(starting_month) + 1) + "/" + str(starting_year)

print sum(days_of_month)










	



