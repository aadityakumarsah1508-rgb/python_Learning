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