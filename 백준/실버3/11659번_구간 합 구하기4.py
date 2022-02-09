import sys
input = sys.stdin.readline
n, m = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.insert(0, 0)
sumnumbers = [0]

for k in range(1, n+1):
    sumnumbers.append(sumnumbers[k-1]+numbers[k])
for _ in range(m):
    i, j = map(int, input().split())
    print(sumnumbers[j]-sumnumbers[i-1])
