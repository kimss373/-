from collections import deque
n, m = map(int, input().split())
miro = [list(input()) for i in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append([0, 0])
while q:
    a, b = q.popleft()
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<=nx<n and 0<= ny<m and miro[nx][ny]=='1':
            q.append([nx, ny])
            miro[nx][ny] = str(int(miro[a][b]) + 1)


print(miro[n-1][m-1])