import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    command = input().strip()
    n = int(input())
    b = input().strip()
    a= deque(b[1:-1].split(','))
    if n == 0:
        a = deque()

    x = 0
    ox = 0
    for i in range(len(command)):
        if command[i] == "R":
            x+= 1
        elif command[i]=="D":
            if len(a) == 0:
                print("error")
                ox=1
                break
            else:
                if x%2==0:
                    a.popleft()
                else:
                    a.pop()
    if ox==1:
        continue
    else:
        if x%2==0:
            print("[" + ",".join(a) + "]")
        else:
            a.reverse()
            print("[" + ",".join(a) + "]")
