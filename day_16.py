# Question 28:- Itertools > itertools.product()

from itertools import product

# Approaching question

# Taking input
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Verifying inputs
print(a)
print(b)

# Printing Cartesian Product
# print(product(a, b)) # it doesn't output anything
pro = list(product(a,b))
print(pro)

# Solution 

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = product(A, B)
print(*result)

# ================================================================================================
# Question 29:- 
from itertools import permutations 
a = list(input().split())
print(a)
k = a[0]
# print(list(permutations([1,2,3], 2)))
RESULT = list(permutations(k, 2))
# print(*RESULT)
for i in RESULT:
    print(*i, sep="")