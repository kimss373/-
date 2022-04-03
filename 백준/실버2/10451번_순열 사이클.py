import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nlist = [i for i in range(1, n+1)]
    nlist.insert(0, 0)
    permutation = list(map(int, input().split()))
    permutation.insert(0, 0)
    cnt = 0
    visit = [0 for _ in range(n)]
    visit.insert(0, 1)
    for j in range(1, n+1):
        if visit[j] == 1:
            continue
        cnt += 1
        visit[j] = 1
        x = j
        while True:
            x = permutation[nlist[x]]
            if visit[x] == 1:
                break
            visit[x] = 1
    print(cnt)