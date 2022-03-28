n = int(input())
podo = []
for _ in range(n):
    podo.append(int(input()))
podo.insert(0, 0)

dp = [0]*(n+1)

dp[1] = podo[1]
if n>1:
    dp[2] = podo[2]+podo[1]


for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-3]+podo[i-1]+podo[i], dp[i-2]+podo[i])

print(dp[n])