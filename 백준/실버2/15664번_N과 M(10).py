import itertools
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = sorted(set(list(itertools.combinations(a, m))))

for i in b:
    for j in i:
        print(j, end=" ")
    print()