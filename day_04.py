# Question 9: - Find the Runner-Up Score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

# score = list(arr)
# winner = max(score)
# runner_up = float('-inf')
# for i in score:
#     if i< winner and i > runner_up:
#         runner_up = i      
# print(runner_up)  

# Another way of doing it  
set_score = sorted(set(arr))
print(set_score[-2])

# =============================================================================================================