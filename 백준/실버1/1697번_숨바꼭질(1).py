from collections import deque
n, k = map(int, input().split())
dp = [0] * 100001


def aaa(x):
    if dp[k] != 0:
        return
    if x-1>= 0 and dp[x-1] == 0:
        dp[x-1] = dp[x]+1
        q.append(x-1)
    if x+1<=100000 and dp[x+1] == 0:
        dp[x+1] = dp[x]+1
        q.append(x+1)
    if 2*x<=100000 and dp[2*x] == 0:
        dp[2*x] = dp[x]+1
        q.append(2*x)


q = deque()
q.append(n)

while q:
    a = q.popleft()
    if a == k:
        break
    aaa(a)

print(dp[k])