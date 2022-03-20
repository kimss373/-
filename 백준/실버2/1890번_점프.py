import sys
input = sys.stdin.readline

n = int(input())
jump = []

for i in range(n):
    a = list(map(int, input().split()))
    jump.append(a)

dp = [[-1]*n for i in range(n)]

def bfs(x, y):
    if x==n-1 and y==n-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0

        x1 = x + jump[x][y]
        y1 = y + jump[x][y]
        if x1<n:
            dp[x][y] += bfs(x1, y)
        if y1<n:
            dp[x][y] += bfs(x, y1)

    return dp[x][y]

z = bfs(0, 0)
print(z)