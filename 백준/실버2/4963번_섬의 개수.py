import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

def bfs(a, b):
    island[b][a] = 0

    for i in range(8):
        if a+dx[i]<0 or a+dx[i]>= w or b+dy[i]<0 or b+dy[i]>=h:
            continue

        if island[b+dy[i]][a+dx[i]] == 1:
            bfs(a+dx[i], b+dy[i])


while True:
    cnt = 0
    w, h = map(int, input().split())
    if w==0 and h==0:
        break

    island = []
    for i in range(h):
        a = list(map(int, input().split()))
        island.append(a)

    for j in range(h):
        for k in range(w):
            if island[j][k]==1:
                bfs(k, j)
                cnt += 1

    print(cnt)