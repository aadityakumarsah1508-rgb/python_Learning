# Question 27:- Collection > collections.Counter()

# understanding the .Counter()

# import collections
from collections import Counter

myList = [1, 2, 3, 4, 1, 2, 3, 4, 5]
myTuple = (1, 2, 3, 4, 5, 1, 4, 3, 4)
myString = "Mr. Selfish"
myDict = {'Aadi':1, 'Shah':5, "Mr.":0, "Selfish":8}

# print(collections.Counter(myList))
print(Counter(myList))
# print(collections.Counter(myTuple))
print(Counter(myTuple))
# print(collections.Counter(myString))
print(Counter(myString))
print(Counter(myDict))