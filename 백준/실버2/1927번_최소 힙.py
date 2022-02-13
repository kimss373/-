import heapq
import sys
input = sys.stdin.readline

n = int(input())

a = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if a:
            print(heapq.heappop(a))
        else:
            print(0)

    else:
        heapq.heappush(a, x)
