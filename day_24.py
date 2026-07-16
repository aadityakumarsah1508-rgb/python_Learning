# Question 36:- Collections > Collections.namedtuple()

from collections import namedtuple

# learning namedtuple
# marks = namedtuple('marks', 'a, b')
# print(marks)

# x = int(input())
# y = int(input())

# x, y = (input().split())
# student1 = marks(a=x, b=y)
# print(student1)
# print(student1.b)


# N = int(input())
# Student = namedtuple('Student', input().split())
# # print(Student)
# for i in range(N):
    
#      = Student(input().split())
# # marks = [int(Student(*input().split()).MARKS) for _ in range(N)]
# # print(f"{sum(marks) / N:.2f}")
# print(Student.ID)    

from collections import namedtuple

N = int(input())
Student = namedtuple('Student', input().split())
marks = [int(Student(*input().split()).MARKS) for _ in range(N)]
print(f"{sum(marks) / N:.2f}")  


# need to learn about this

    