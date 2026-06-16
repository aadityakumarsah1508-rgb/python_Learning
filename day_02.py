# Python Day - 02

# Question 1 - Python If-Else (Hackerrank)
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        # if n >= 2 and n <= 5:
        if 2 <= n <=5:
            print("Not Weird")
        # elif n >=6 and n <= 20:
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")

# ========================================================================================================

# Question 2 - Arithmetic Operators (Hackerrank)
    a = int(input())
    b = int(input())
    
    sum = a + b
    print(sum)
    diff = a - b
    print(diff)
    pro = a * b
    print(pro)

# ============================================================================================================

# Question 3 - Python: Division (Hackerrank)
    a = int(input())
    b = int(input())
    
    div = a//b
    print(div)
    
    div1 = float(a/b)
    print(div1)

# ============================================================================================================

# Question 4 - Loops (Hackerrank)
    n = int(input())
    
    for i in range(0,n):
        print(i*i)

# ===========================================================================================================

# Question 5 - Write a fuction 

def is_leap(year):
    leap = False
    
    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    if year % 400 == 0:
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))