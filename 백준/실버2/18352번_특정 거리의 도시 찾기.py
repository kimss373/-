import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visit = [0 for i in range(n+1)]
visit[x] = 1

cnt = 1
tmp = [x]
while cnt<=k:
    if tmp:
        for _ in range(len(tmp)):
            start = tmp.pop(0)
            for i in graph[start]:
                if visit[i] == 0:
                    visit[i] = 1
                    tmp.append(i)

    else:
        break

    cnt += 1

if tmp:
    tmp.sort()
    for i in tmp:
        print(i)
else:
    print(-1)