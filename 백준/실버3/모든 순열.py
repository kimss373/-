n = int(input())

result = []
visit = [0 for i in range(n)]

def permutation(tot, depth):
    global visit
    global result
    if depth == tot+1:
        print(' '.join(result))
        return
    for i in range(n):
        if visit[i] == 0:
            result.append(str(i+1))
            visit[i] = 1
            permutation(tot, depth+1)
            result.pop()
            visit[i] = 0

permutation(n, 1)

