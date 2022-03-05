import sys
import itertools
import math

input = sys.stdin.readline
t = int(input())

for i in range(t):
    a = list(map(int, input().split()))
    n = a.pop(0)
    combi = list(itertools.combinations(a, 2))
    cnt = 0
    for j in combi:
        cnt += math.gcd(j[0], j[1])
    print(cnt)