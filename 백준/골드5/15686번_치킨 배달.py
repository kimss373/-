import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
city = []
for _ in range(n):
    row = list(map(int, input().split()))
    city.append(row)

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

result = []
for k in combinations(chicken, m):
    temp = 0
    for l in house:
        length = 9999
        for v in range(m):
            length = min(length, abs(l[0]-k[v][0]) + abs(l[1]-k[v][1]))
        temp += length
    result.append(temp)

print(min(result))