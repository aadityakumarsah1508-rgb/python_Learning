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

# solution of question
if __name__ == '__main__':
    s = input()
    
    print(any(l.isalnum() for l in s))
    print(any(l.isalpha() for l in s))
    print(any(l.isdigit() for l in s))
    print(any(l.islower() for l in s))
    print(any(l.isupper() for l in s))

# =========================================================================================================

# Question 20