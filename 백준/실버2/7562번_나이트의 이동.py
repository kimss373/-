from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [-2, -2, -1, 1, 2, 2, 1, -1]

def bfs(a, b, c, d):
    q = deque()
    q.append([a, b])
    s[a][b] = 1
    while q:
        x, y = q.popleft()
        if x==c and y==d:
            print(s[c][d]-1)
            return

        for i in range(8):
            g = x + dx[i]
            h = y + dy[i]
            if 0<=g<l and 0<=h<l and s[g][h] == 0:
                q.append([g, h])
                s[g][h] = s[x][y] +1

t= int(input())
for _ in range(t):
    l = int(input())
    startx, starty = map(int, input().split())
    endx, endy = map(int, input().split())
    s = [[0]*l for i in range(l)]
    bfs(startx, starty, endx, endy)

