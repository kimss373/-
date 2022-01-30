n = int(input())
a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

dp = [0]*(n+1)

for i in range(n-1, -1, -1):
    dp[i] = dp[i+1]
    if a[i][0] + i <= n:
        dp[i] = max(dp[i], dp[i+a[i][0]]+a[i][1])

print(dp[0])

# [0, 0, 0, 15, 15, 0, 0, 0]