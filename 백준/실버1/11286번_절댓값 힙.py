import sys
import heapq
numbers = int(input())
input = sys.stdin.readline
heap = []
for _ in range(numbers):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)