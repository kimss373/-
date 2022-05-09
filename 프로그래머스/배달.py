import heapq

def solution(N, road, K):
    answer = 0
    inf = 500001
    dp = [inf for i in range(N+1)]
    graph = [[] for _ in range(N+1)]
    for _ in range(len(road)):
        a, b, c = road[_]
        graph[a].append([b, c])
        graph[b].append([a, c])

    q = []
    heapq.heappush(q, [0, 1])
    dp[1] = 0

    while q:
        dist, node = heapq.heappop(q)
        if dp[node] < dist:
            continue

        for i in graph[node]:
            cost = dp[node] + i[1]
            if cost < dp[i[0]]:
                dp[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

    for i in dp:
        if i<=K:
            answer += 1
    return answer
print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))