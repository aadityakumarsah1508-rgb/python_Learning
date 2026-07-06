# Question 27:- Collection > collections.Counter()

# understanding the .Counter()

# import collections
from collections import Counter

# myList = [1, 2, 3, 4, 1, 2, 3, 4, 5]
# myTuple = (1, 2, 3, 4, 5, 1, 4, 3, 4)
# myString = "Mr. Selfish"
# myDict = {'Aadi':1, 'Shah':5, "Mr.":0, "Selfish":8}

# # print(collections.Counter(myList))
# print(Counter(myList))
# # print(collections.Counter(myTuple))
# print(Counter(myTuple))
# # print(collections.Counter(myString))
# print(Counter(myString))
# print(Counter(myDict))

# Understanding the question
x = 10 # no. of shoe
list = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18] # space generated list
n = 6 # no. of customer
# xi will be the price of shoe
# no. of user input values = no. of customer

sample_input = [6, 55] # where 6 is size of shoe and 55 is price

# Output will be the total money
# Approaching the question

final_price = 0
# Taking input from user
for i in range(n):
    customer_demand = input().split()

print(customer_demand)