import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

da = [0, 0, 1, -1]
db = [1, -1, 0, 0]

def bfs(arr, a, b):
    queue = deque()
    queue.append((a, b))
    arr[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + da[i]
            ny = y + db[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = 0
    return

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    arr = []
    for i in range(n):
        list = [0]*m
        arr.append(list)

    for j in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for k in range(n):
        for l in range(m):
            if arr[k][l] == 1:
                bfs(arr, k, l)
                cnt += 1
    print(cnt)