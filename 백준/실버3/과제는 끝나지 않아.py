import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q = deque()

answer = 0
for i in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        q.append(cmd[1:])

    if q:
        q[-1][1] -= 1
        if q[-1][1] == 0:
            x = q.pop()
            answer += x[0]

print(answer)