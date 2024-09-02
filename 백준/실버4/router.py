from collections import deque
import sys

input = sys.stdin.readline
q = deque()

n = int(input())

while True:
    tmp = int(input())
    if tmp == -1:
        break
    elif tmp == 0:
        q.popleft()
    else:
        if len(q) < n:
            q.append(tmp)

if len(q) == 0:
    print('empty')
else:
    for i in range(len(q)):
        print(q.popleft(), end=" ")