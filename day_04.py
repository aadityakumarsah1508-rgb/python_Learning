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

# Question 10:- Nested List

if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
        
n_sorte = sorted(student, key=lambda x: (x[1], x[0]))
# print(n_sorte)

smallest = (n_sorte[0])

for i in n_sorte:
    if i[1] > smallest[1]:
        smallest = i
        break
        
for n in n_sorte:
    if n[1] == smallest[1]:
        print(n[0])

