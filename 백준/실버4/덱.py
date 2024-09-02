import sys
input = sys.stdin.readline

n = int(input())

deque = []
for _ in range(n):
    command = list(map(str, input().split()))
    if command[0] == 'push_back':
        deque.append(int(command[1]))
    elif command[0] == 'push_front':
        deque.insert(0, int(command[1]))
    elif command[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif command[0] == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    else:
        if deque:
            print(deque.pop())
        else:
            print(-1)