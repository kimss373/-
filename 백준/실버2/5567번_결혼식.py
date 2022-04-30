n = int(input())
m = int(input())
chodae = [[] for i in range(n+1)]
visit = [0 for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    chodae[a].append(b)
    chodae[b].append(a)

for i in chodae[1]:
    visit[i] = 1
    for j in chodae[i]:
        visit[j] = 1
visit[1] = 0

print(visit.count(1))