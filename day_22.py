# Question 34: - Date and Time > Calendar Module

import calendar

# Taking Input
# m, d, y = int(input().split())
m, d, y = map(int, input().split())
# print("Printing the Date: ", d, m, y)

# Attempting the question
day = calendar.weekday(year=y, month=m, day=d)

print(day)

