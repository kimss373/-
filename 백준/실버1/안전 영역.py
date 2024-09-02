from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]

max = 0
q = deque()
for depth in range(1, 101):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if land[i][j] > depth:
                