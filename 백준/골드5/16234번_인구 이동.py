import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
n, l, r = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]
day= 0

while True:
    visit = [[0 for _ in range(n)] for _ in range(n)]
    tmpday = 0
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                people = 0
                cnt = 0
                result = []
                q.append([i, j])
                result.append([i, j])
                while q:
                    x, y = q.popleft()
                    cnt += 1
                    people += world[x][y]
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and l <= abs(world[x][y] - world[nx][ny]) <= r:
                            visit[nx][ny] = 1
                            q.append([nx, ny])
                            result.append([nx, ny])
                z = people//cnt
                for v in result:
                    world[v[0]][v[1]] = z
                if len(result) >= 2:
                    tmpday = 1
    if tmpday == 1:
        day += 1
    if tmpday == 0:
        break


print(day)

