import sys
n = list(sys.stdin.readline().strip())

m = int(input())

stack = []
for _ in range(m):
    i = sys.stdin.readline()

    if i[0] == 'B':
        if n:
            n.pop()
        else:
            continue

    elif i[0] == 'L':
        if n:
            stack.append(n.pop())
        else:
            continue
    elif i[0] == 'D':
        if stack:
            n.append(stack.pop())
        else:
            continue
    elif i[0] == 'P':
        n.append(i[2])
for k in n:
    print(k, end="")
for j in reversed(stack):
    print(j, end="")