n = int(input())

dp = [i for i in range(n+1)]

for i in range(1, n+1):
    a = []
    for j in range(1, i):
        if j*j > i:
            break
        a.append(dp[i-j*j])
    if a:
        dp[i] = min(a) +1

print(dp[n])