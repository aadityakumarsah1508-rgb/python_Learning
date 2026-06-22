# Question 13:- Tuples

# this question solved only in language PyPy2

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    t = tuple(integer_list)
    print(hash(t))

# =============================================================================================

# Question 14:- sWAP cASE

def swap_case(s):
    line = s.swapcase()
    return line

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# =============================================================================================

# Question 15:- 