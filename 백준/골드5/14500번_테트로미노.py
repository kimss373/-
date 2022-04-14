import sys; input=sys.stdin.readline

n, m = map(int, input().split())
tetro = []
for _ in range(n):
    row = list(map(int, input().split()))
    tetro.append(row)

visit = [([0]*m) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, tetro)) #    tetro라는 배열에서 가장 큰 값
def dfs(x, y, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if idx == 1:
                    visit[nx][ny] = 1
                    dfs(x, y, idx+1, total + tetro[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                dfs(nx, ny, idx+1, total + tetro[nx][ny])
                visit[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 0, tetro[i][j])
        visit[i][j] = 0
print(ans)
