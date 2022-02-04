n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))
cnt = 0
for j in range(n-1, -1, -1):
    if k//coins[j]>= 1:
        cnt += k//coins[j]
        k = k%coins[j]

print(cnt)