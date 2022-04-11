import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())

nummap = []
for _ in range(n):
    nummap.append(list(map(int, (input().rstrip()))))

def findway():
    q = deque()
    q.append([0, 0, 0])
    visit = []
    for _ in range(n):
        visit.append([[0, 0] for _ in range(m)])
    visit[0][0][0] = 1

    while q:
        x, y, wall = q.popleft()
        if x==n-1 and y==m-1:
            return visit[x][y][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny][wall] == 0:
                if nummap[nx][ny] == 0:
                    q.append([nx, ny, wall])
                    visit[nx][ny][wall] = visit[x][y][wall] + 1

                if wall==0 and nummap[nx][ny] == 1:
                    q.append([nx, ny, 1])
                    visit[nx][ny][1] = visit[x][y][0] +1

    return -1

print(findway())