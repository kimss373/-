answer = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n, m = map(int, input().split())

tetro = []

for i in range(n):
    inp = list(map(int, input().split()))
    tetro.append(inp)

visit = [[0 for i in range(m)] for j in range(n)]
max_val = max(map(max, tetro))

def dfs(x, y, cnt, sum):
    global answer
    if answer >= sum + max_val * (3-cnt):
        return
    if cnt==3:
        answer = max(answer, sum)

        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0 <=ny<m and visit[nx][ny] == 0:
            if cnt == 1:
                visit[nx][ny] = 1
                dfs(x, y, cnt+1, sum+tetro[nx][ny])
                visit[nx][ny] = 0
            visit[nx][ny] = 1
            dfs(nx, ny, cnt + 1, sum + tetro[nx][ny])
            visit[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 0, tetro[i][j])
        visit[i][j] = 0

print(answer)



