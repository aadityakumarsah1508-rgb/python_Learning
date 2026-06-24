# Question 20:- Merge the tools

# Question Statement
s = 'AABCAAADA'
k = 3

n = len(s)
q = n/k

# Trying to Finding logics 
substring = []
p = s[0:3]
q = s[3:6]
r = s[6:9]
print(p, q, r)

# Inistating the Substring 
for i in range(len(s)):
    if i%k == 0:
        a = s[i:(i+k)]
        substring.append(a)
        print(i)
print(substring)

