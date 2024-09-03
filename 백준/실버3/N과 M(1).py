from collections import deque
q = deque()

n, m = map(int, input().split())

visit = [0 for i in range(n)]

def permutate(num, depth):
    global q
    global visit
    if depth == m:
        print(' '.join(map(str, q)))
        return
    for i in range(num):
        if visit[i] == 0:
            q.append(i+1)
            visit[i] = 1
            permutate(num, depth+1)
            visit[i] = 0
            q.pop()

permutate(n, 0)