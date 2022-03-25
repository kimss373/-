n = int(input())

triangle = []
dp = []
for _ in range(n):
    a = list(map(int, input().split()))
    triangle.append(a)

for i in range(n):
    b = [0]*(i+1)
    dp.append(b)

dp[0][0] = triangle[0][0]

for j in range(1, n):
    for k in range(j+1):
        if k == 0:
            dp[j][0] = dp[j-1][0] + triangle[j][0]
        elif k==j:
            dp[j][j] = dp[j-1][j-1] + triangle[j][j]
        else:
            dp[j][k] = max(dp[j-1][k-1], dp[j-1][k]) + triangle[j][k]

print(max(dp[n-1]))