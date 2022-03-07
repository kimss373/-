from collections import deque

def dfs(a):
    visited[a] = True
    print(a, end=" ")
    for i in tree[a]:
        if not visited[i]:
            dfs(i)

def bfs(b):
    queue = deque([b])
    visited[b] = True
    while queue:
        c=queue.popleft()
        print(c, end=" ")
        for i in tree[c]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
tree = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)
for i in range(1, n+1):
    tree[i].sort()

visited = [False]*(n+1)

dfs(v)
print()
visited = [False]*(n+1)
bfs(v)