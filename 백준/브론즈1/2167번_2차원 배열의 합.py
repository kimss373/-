import sys
n, m = map(int, sys.stdin.readline().split())
a=[tuple(map(int, input().split())) for i in range(n)]
for _ in range(int(sys.stdin.readline())):
    i, j, x, y = map(int, sys.stdin.readline().split())
    b=0
    for k in range(i-1, x):
        b += sum(a[k][j-1:y])
    print(b)