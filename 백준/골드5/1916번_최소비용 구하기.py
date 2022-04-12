import sys
from collections import deque
input = sys.stdin.readline

inf = 1e9

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
dp = [inf for _ in range(n+1)]
heap = deque()

for i in range(m):
    a, b, price = map(int, input().split())
    graph[a].append([b, price])

depart, arrive = map(int, input().split())
dp[depart] = 0
heap.append([0, depart])
while heap:
    x, y = heap.popleft()
    if dp[y]<x:
        continue
    for n_n, wei in graph[y]:
        n_w = wei + x
        if n_w < dp[n_n]:
            dp[n_n] = n_w
            heap.append([n_w, n_n])


print(dp[arrive])