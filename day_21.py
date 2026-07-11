# Question 33:- Collections > DefaultDict Tutorial

from collections import defaultdict

# Taking input from user
n, m = list(map(int, input().split()))

group1 = []
group2 = []

for i in range(n):
    group1.append(input())

for i in range(m):
    group2.append(input())

d = defaultdict()

# Appraoching the Question
for i in group2:
    if i in group1:
        # print(i) -- it print the character itself we have to get its index
        # print(group1.index(i)) -- it also doesn't work as it return only the first occurence
        # we have to use enumerate
        # print([i for i, x in enumerate(group1) if i in group1 ])
        d[i] = [a +1 for a, x in enumerate(group1) if x == i]
        # print(d) 
        print(" ".join(map(str, d[i])))
    else:
        print(-1)
