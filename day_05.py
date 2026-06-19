# Question 11:- Finding the Percentage

# This is how i actually debug and try to solve line by line.

# stud = {
#     'aadi':[1,2,3,4],
#     'wadi':[5,6,7,8]
#     }

# print(stud['aadi'])
# l = len('aadi')
# sum = 0
# avg = 0
# for i in stud['aadi']:
#     sum = sum + i
# avg = sum/l
# # avg = float(sum/l)
# avg = round(avg,2)
# print("Average is",avg)

# Understandig the how the question work
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

# student_marks = {
#     'aadi':[1,2,3,4],
#     'wadi':[5,6,7,8]
#     }
# query_name = input("query name ")

# print(student_marks[query_name])
# leg = len(query_name)
# print(leg)
 
sum = 0
for i in student_marks[query_name]:

    sum = float(sum + i)


avg = round(sum/len(student_marks[query_name]), 2)
print(f"Average of {avg:.2f}")
