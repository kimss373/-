from collections import deque
n = int(input())
danzi = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []

q = deque()
z = 1
for i in range(n):
    for j in range(n):
        if danzi[i][j] == 1:
            z += 1
            q.append([i, j])
            cnt = 0
            while q:
                a, b = q.popleft()
                danzi[a][b] = z
                cnt += 1
                for k in range(4):
                    nx = a + dx[k]
                    ny = b + dy[k]
                    if 0<=nx<n and 0<=ny<n and danzi[nx][ny] == 1 and [nx, ny] not in q:
                        q.append([nx,ny])
            result.append(cnt)

print(len(result))
result.sort()
p = 1
for l in result:
    print(l)
