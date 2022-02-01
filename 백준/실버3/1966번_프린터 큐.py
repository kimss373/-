t=int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    deque = []
    for i in range(len(queue)):
        deque.append((queue[i],i))

    answer = 0
    while True:
        if max(queue) == deque[0][0]:
            if deque[0][1] == m:
                queue.pop(0)
                deque.pop(0)
                answer += 1
                break
            else:
                queue.pop(0)
                deque.pop(0)
                answer += 1

        else:
            queue.append(queue.pop(0))
            deque.append(deque.pop(0))

    print(answer)