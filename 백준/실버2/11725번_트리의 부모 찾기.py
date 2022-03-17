import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
a = [[] for i in range(n+1)]
parents = [0]*(n+1)

for i in range(n-1):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

def DFS(start):
    for i in a[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i)

DFS(1)

for j in range(2, n+1):
    print(parents[j])