import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
result = [INF for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

start, end = map(int, input().split())
result[start] = 0
q = []

heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)

    if result[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]

        if cost<result[i[0]]:
            result[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

print(result[end])