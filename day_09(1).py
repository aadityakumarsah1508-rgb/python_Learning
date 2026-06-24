# Question 20:- Merge the tools

# Question Statement
s = 'AABCAAADA'
k = 3

n = len(s)
q = n/k

# # Trying to Finding logics 
# substring = []
# p = s[0:3]
# q = s[3:6]
# r = s[6:9]
# print(p, q, r)

# # Inistating the Substring 
# for i in range(len(s)):
#     if i%k == 0:
#         a = s[i:(i+k)]
#         substring.append(a)
#         print(i)
# print(substring)

# after getting a help with AI
substr = [s[i:i+k] for i in range(0, len(s), k)]
# [s[i:i+k] for i in range(0, len(s), k)]
print(substr)
#----------------------------------------------------------------

for i in range(len(substr)):
    # print(map(f't{i}',substr.split()))
    pass

# u = []
# for i in substr:
#     for j in range(len(i)):
#         # 'U{j}' = i[j] + i[j+1]
#         # print(i[j])
# #         print(u)

#         # if i[j - 1] != i[j]:
#         #     u.append(i[j])

#         # if i[j] not in u:
#         #     substr[j] = u.append(i[j])
# print(u)

for i in substr:
     print(*(set(i)), sep="")


# =======================================================================

# final answer

string = 'AABCAAADA'

n = len(string)
q = int(n/k)
    
substr = [string[i:i+k] for i in range(0, n, k)]
    
for i in substr:
    print(*(set(i)), sep="")