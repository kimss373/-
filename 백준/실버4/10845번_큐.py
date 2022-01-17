import sys
n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if len(command) == 2:
        queue.append(command[1])

    else:
        if 'back' in command:
            if queue:
                print(queue[-1])
            elif not queue:
                print(-1)

        elif 'front' in command:
            if queue:
                print(queue[0])
            elif not queue:
                print(-1)

        elif 'pop' in command:
            if queue:
                print(queue.pop(0))
            elif not queue:
                print(-1)

        elif 'size' in command:
            print(len(queue))

        else:
            if queue:
                print(0)
            elif not queue:
                print(1)