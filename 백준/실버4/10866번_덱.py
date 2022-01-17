import sys
n = int(sys.stdin.readline())
deque = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if len(command) == 2:
        if 'front' in command[0]:
            deque.insert(0, command[1])
        elif 'back' in command[0]:
            deque.append(command[1])

    elif 'pop_front' in command:
        if deque:
            print(deque.pop(0))
        elif not deque:
            print(-1)

    elif 'pop_back' in command:
        if deque:
            print(deque.pop())
        elif not deque:
            print(-1)

    elif 'size' in command:
        print(len(deque))

    elif 'front' in command:
        if deque:
            print(deque[0])
        elif not deque:
            print(-1)

    elif 'back' in command:
        if deque:
            print(deque[-1])
        elif not deque:
            print(-1)

    else:
        if deque:
            print(0)
        elif not deque:
            print(1)