# Question 37: Date and Time > Time Delta

# Learing python Date from W3school
# datetime module is used to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)

# methods in datetime module
print(x.year) # it returns the year
print(x.strftime("%A")) # it return the name of the weekday

# there are diff diff reference for fomat the code:

# Solution
def time_delta(t1, t2):

    fmt = "%a %d %b %Y %H:%M:%S %z"
    
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    
    seconds = str(abs(int((dt1 - dt2).total_seconds())))
    return seconds

# main function goes here.....
