# Question 23:- String > Designer door mat

# Approaching the question
n = 11
m = 33

z = 27//2
# print(z)
a = ".|."

# Applying ideas
# print(a.center(21,"-"))
# print(a.center(24,"-"))

# Idea - Using nested loop to print 
# for i in range(n):
#     print("welcome".center(21, "-"))
#     for j in range(m):
#         print("H", end="")
#         a.center(21, "-")
#         print("-" * z + a + "-"*z)
#     print()

# Idea - print using odd numbers
# for i in range(7):
    # printing things before 
# for j in range(7):
#         if j%2!=0:
#             print((a*j).center(21, "-"))
# print("WELCOME")

# Trying to back loop
# for j in range(7,-1):
#         if j%2!=0:
#             print((a*j).center(21, "-"))

# for i in range(6, 0, -2):
#       print((a*i).center(21, "-"))

    # print((a*5).center(21, "-"))


# Solution 

# Printing lines before the Welcome line
for i in range(n):
    if i % 2 != 0:
        print((a*i).center(m, "-"))

# printing the welcome line
print("WELCOME".center(m, "-"))

#printing the lines after welcome line
# for i in range(7, 0, -1):  # error comes as it is hard coded
# for i in range(n, 0, -1): # error - printing an xtra line 
for i in range((n-1), 0, -1):
    if i % 2 != 0:
        print((a*i).center(m, "-"))


# ==============================================================================================

# Question 24:- String > String Formating 

number = 17
print(number + oct(number) + "\t" + hex(number) + "\t" + bin(number) + "\t") 
# Upper line gives error as it number is int type while the rest is of string type.

for i in range(number):
    print( str(i) + "\t" + oct(i) +  "\t" + hex(i) + "\t" + bin(i)) # it doesn't work as space is too much 
    # result is different required output is different 
    print(str(i) + " " + oct(i)[2:] + " " + hex(i)[2:] + " " + bin(i)[2:]) # it also produces error as space not matched



