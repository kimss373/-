import heapq
import sys
input = sys.stdin.readline
max_heap = []

n = int(input())
for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(max_heap, (-x, x))
    else:
        if max_heap:
            y = heapq.heappop(max_heap)
            print(y[1])
        else:
            print(0)