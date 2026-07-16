# Question 36:- Collections > Collections.namedtuple()

from collections import namedtuple

# learning namedtuple
marks = namedtuple('marks', 'a, b')
print(marks)

# x = int(input())
# y = int(input())

x, y = (input().split())
student1 = marks(a=x, b=y)
print(student1)
print(student1.b)




    