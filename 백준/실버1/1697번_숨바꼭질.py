from collections import deque
n, k = map(int, input().split())
dp = [0] * 100001


def aaa():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x==k:
            print(dp[x])
            return
        if 100000>=x-1>= 0 and dp[x-1] == 0:
            dp[x-1] = dp[x]+1
            q.append(x-1)
        if 0<=x+1<=100000 and dp[x+1] == 0:
            dp[x+1] = dp[x]+1
            q.append(x+1)
        if 0<=2*x<=100000 and dp[2*x] == 0:
            dp[2*x] = dp[x]+1
            q.append(2*x)

aaa()