n, m = map(int, input().split())
candy = []
for i in range(n):
    row = list(map(int, input().split()))
    candy.append(row)

dp = [[0]*(m+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = candy[i-1][j-1] + max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
print(dp[n][m])