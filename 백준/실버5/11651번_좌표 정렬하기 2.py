import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((y, x))
arr.sort()
for j in arr:
    print(j[1], j[0])