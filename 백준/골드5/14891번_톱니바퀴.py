from collections import deque
q = deque()
topni = []
for _ in range(4):
    row = list(input())
    topni.append(row)

k = int(input())
for i in range(k):
    action = []
    visit = [0, 0, 0, 0]
    bun, direct = map(int, input().split())
    x = bun-1
    q.append([x, direct])
    action.append([x, direct])
    visit[x] = 1
    while q:
        a, b = q.popleft()
        if a+1<4 and visit[a+1] ==0:
            if topni[a][2] != topni[a+1][6]:
                q.append([a+1, -1*b])
                action.append([a+1, -1*b])
                visit[a+1] = 1
        if a-1>=0 and visit[a-1] == 0:
            if topni[a][6] != topni[a-1][2]:
                q.append([a-1, -1*b])
                action.append([a-1, -1*b])
                visit[a-1] = 1

    for j in action:
        idx, action = j
        if action == 1:
            topni[idx].insert(0, topni[idx].pop())
        else:
            topni[idx].append(topni[idx].pop(0))

answer = 0
for k in range(4):
    if topni[k][0] == '1':
        answer += 2**k

print(answer)
