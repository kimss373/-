from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
location = [-1 for i in range(f)]
button = [u, -d]
location[s-1] = 0
q = deque()
q.append(s-1)
visit = [0 for i in range(f)]
visit[s-1]= 1
while q:
    x = q.popleft()
    for i in range(2):
        nx = x + button[i]
        if 0<=nx<f and visit[nx] == 0:
            q.append(nx)
            location[nx] = location[x]+1
            visit[nx] = 1

if location[g-1] != -1:
    print(location[g-1])
else:
    print("use the stairs")