import sys

input = sys.stdin.readline

n = int(input())
set1 = set(map(int, input().split()))

m = int(input())
list2 = list(map(int, input().split()))

for i in range(m):
    if list2[i] in set1:
        print(1)
    else:
        print(0)