# Question 30:- Stings > The minions game

s = input()

kevin_score = 0
sturt_score = 0

vowelS = set("AEIOU")

# len = len(s)
# print(len)

# doesn't working   ------------- its not working as i have set vowel[AEIOU] and input string in smallcase. 
# for i in range(len):
#     # print(s[i]+"For loop with i")
#     for j in range(len-i):
#         # print(s[j]+"J loop")
#         if s[i] in vowelS:
#             print(s[j:])
#     # if s[i] not in vowelS:
#     #     print(s[i:])
# 🤯🤯🤯😤😤😤😤


# for i in range(len(s)):
#     # print(s[i])
#     if s[i] in vowelS:
#         kevin_score += (len(s) - i)
#         # print("ues")
#     elif s[i] not in vowelS:
#         # print("not")
#         sturt_score += len(s)-i

# print("kwcin = ", kevin_score)
# print("sturt = ", sturt_score)

# if kevin_score > sturt_score:
#     print("Kevin", kevin_score)
# elif kevin_score < sturt_score:
#     print("Stuat ", sturt_score)
# else:
#     print("Draw")

# ================================================================================================

# Solution: -

def minion_game(string):
    # your code goes here
    kevin_score = 0
    stuart_score = 0
    vowels = set("AEIOU")
    for i in range(len(s)):
        if s[i] in vowels:
            kevin_score += (len(s) - i)
        elif s[i] not in vowels:
            stuart_score += len(s)-i

    # print("kwcin = ", kevin_score)
    # print("sturt = ", stuart_score)

    # checking whoes is winner
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)