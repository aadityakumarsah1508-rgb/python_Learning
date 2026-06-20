# Question  12: - Lists

N = int(input())
lis = []
for _ in range(N):
    query, *values = input().split()
    value = list(map(int,values))
        
    if query == 'insert':
        lis.insert(value[0],value[1])
    if query == 'print':
        print(lis)
    if query == 'remove':
        lis.remove(value[0])
    if query == 'append':
        lis.append(value[0])
    if query == 'sort':
        lis.sort()
    if query == 'pop':
        lis.pop()
    if query == 'reverse':
        lis.reverse()


