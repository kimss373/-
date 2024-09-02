import sys
input = sys.stdin.readline

front = list(input().rstrip())
back = []
m = int(input())

for _ in range(m):
    command = list(input().split())
    if command[0] == 'L':
        if front:
            back.append(front.pop())
    elif command[0] == 'D':
        if back:
            front.append(back.pop())
    elif command[0] == 'B':
        if front:
            front.pop()
    else:
        front.append(command[1])
front.extend(reversed(back))
print(''.join(front))
