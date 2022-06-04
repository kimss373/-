import sys
import heapq
input = sys.stdin.readline

INF = 1e9
n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

price = [INF for i in range(n+1)]
price[1] = 0

hq = []
heapq.heappush(hq, [0, 1])
while hq:

    x, y = heapq.heappop(hq)
    for a, b in graph[y]:
        money = x + b
        if money<price[a]:
            price[a]=money
            heapq.heappush(hq, [money, a])


print(price[n])