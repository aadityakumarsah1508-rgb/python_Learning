# Question 34: - Date and Time > Calendar Module

import calendar

# Taking Input
# m, d, y = int(input().split())
m, d, y = map(int, input().split())
# print("Printing the Date: ", d, m, y)

# Attempting the question
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.firstweekday())

day = calendar.weekday(year=y, month=m, day=d)

print(day)

# Remember Python treat 0 as Monday, 1 Tuesday and so on.
 
if day == 0:
    print("MONDAY")
elif day == 1:
    print("TUESDAY")
elif day == 2:
    print("WEDNESSDAY")
elif day == 3:
    print("THRUSDAY")
elif day == 4:
    print("FRIDAY")
elif day == 5:
    print("SATURDAY")
elif day == 6:
    print("SUNDAY")