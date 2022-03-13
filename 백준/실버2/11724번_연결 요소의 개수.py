import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(a):
    visited[a] = True
    for e in link[a]:
        if not visited[e]:
            dfs(e)

n, m = map(int, input().split())
link = [[] for i in range(n+1)]
visited = [False]*(n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        cnt += 1

print(cnt)