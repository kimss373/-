n = int(input())
a = list(map(int, input().split()))
dp = [0]*n

a = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]

for i in range(n):
    for j in range(i):
        if a[i]>a[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i] += 1