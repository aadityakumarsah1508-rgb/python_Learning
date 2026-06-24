# Question 19:- String Validator

# trying the methods
s = 'Aadi1508'
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.islower())
# print(s.isupper())

# Approaching the question

# l = []
# for i in s:
#     # l.append(i.isupper())
#     print('True' ) if any(i.isupper()) else print('False')

# # print(l)
# # print(any(l))

# final verdict
print(any(l.isalnum() for l in s))

