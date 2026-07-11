# Question 33:- Collections > DefaultDict Tutorial

from collections import defaultDict

# Taking input from user
n, m = list(map(str, input().split()))

group1 = []
group2 = []

for i in range(n):
    group1.append(input())

for i in range(m):
    group2.append(input())