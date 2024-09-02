from collections import deque

n = int(input())
x = int(input())

arr = [[] for i in range(n+1)]

for _ in range(x):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visit = [False for _ in range(n+1)]
visit[1] = True
answer = 0

q = deque()
for i in arr[1]:
    q.append(i)
    visit[i] = True
    answer += 1

while q:
    go = q.popleft()
    for i in arr[go]:
        if not visit[i]:
            answer += 1
            q.append(i)
            visit[i] = True

print(answer)