# Question 35:- Errors and Exceptions > Exceptions

# taking input
# T = int(input())
# for _ in range(T+1):
#     a, b = input().split()

# Approaching the question:- 

# try:
#     T = int(input())
#     for _ in range(T+1):
#         a, b = input().split()
#         print(int(a)/int(b))
# except(ZeroDivisionError | ValueError)as e:
#     print("Error COde:",e)

# T = int(input())
# for _ in range(T):
#     row = list(input().split())
# print(row)

# ==========================================================

# try:
#     pass
# except(ZeroDivisionError | ValueError)as e:
#     print("Error COde:",e)

# ==========================================================

# T = int(input())
# ls =[]
# for _ in range(T):
#     # row = input().split()
#     row = list(input().split())
#     ls.append(row)
# # print(ls)

# for i in range(len):
#     try:
#         a = int(ls[i][0])
#         b = int(ls[i][1])
        
#         print(a//b)
#     except ValueError as e:
#         print("Error code:", e)
#     except ZeroDivisionError as e:
#         print("Error code:", e)
# # this also doesn't workk as in qustion we have to take inout at once and then execute the code.    

# ===============================================================================
# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
ls =[]
for _ in range(T):
    # row = input().split()
    row = list(input().split())
    ls.append(row)
# print(ls)

for i in range(len(ls)):
    try:
        a = int(ls[i][0])
        b = int(ls[i][1])
        print(a//b)
        
    except ZeroDivisionError as e:
        # print("Error code:", e)
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)


# Optimizing the Code: --

# Read the number of test cases
T = int(input())

# Process each test case immediately (no extra list needed)
for _ in range(T):
    try:
        a, b = input().split()
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)