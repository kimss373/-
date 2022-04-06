import sys
from heapq import heappush, heappop
input = sys.stdin.readline

inf = 1e9
v, e = map(int, input().split())
k = int(input())
graph = [[]for _ in range(v+1)]
dp = [inf for _ in range(v+1)]
heap = []

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

dp[k] = 0
heappush(heap, [0, k])
while heap:    # heap
    x, y = heappop(heap)
    for n_n, wei in graph[y]:
        n_w = wei + x
        if n_w < dp[n_n]:
            dp[n_n] = n_w
            heappush(heap, [n_w, n_n])
[inf, 0, 2, 3, 7, inf]

for i in dp[1:]:
    if i != inf:
        print(i)
    else:
        print("INF")