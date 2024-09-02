import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

stack = []

arr = deque()

for i in range(n):
    tmp = list(map(str, input().split()))
    if tmp[0] == '1':
        arr.append(tmp[1])
        stack.append('1')
    elif tmp[0] == '2':
        arr.appendleft(tmp[1])
        stack.append('2')
    else:
        if arr:
            tmp1 = stack.pop()
            if tmp1 == '1':
                arr.pop()
            else:
                arr.popleft()

if arr:
    print(*arr,sep="")
else:
    print(0)

