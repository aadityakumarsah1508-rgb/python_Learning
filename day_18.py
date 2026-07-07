# Question 30:- Stings > The minions game

s = input()

kevin_score = 0
sturt_score = 0

vowelS = set("AEIOU")

# len = len(s)
# print(len)

# doesn't working 
# for i in range(len):
#     # print(s[i]+"For loop with i")
#     for j in range(len-i):
#         # print(s[j]+"J loop")
#         if s[i] in vowelS:
#             print(s[j:])
#     # if s[i] not in vowelS:
#     #     print(s[i:])
# 🤯🤯🤯😤😤😤😤


for i in range(len(s)):
    # print(s[i])
    if s[i] in vowelS:
        kevin_score += (len(s) - i)
        # print("ues")
    elif s[i] not in vowelS:
        # print("not")
        sturt_score += len(s)-i

print("kwcin = ", kevin_score)
print("sturt = ", sturt_score)

if kevin_score > sturt_score:
    print("Kevin", kevin_score)
elif kevin_score < sturt_score:
    print("Stuat ", sturt_score)
else:
    print("Draw")