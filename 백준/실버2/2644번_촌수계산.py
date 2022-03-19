from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
chon = [[] for _ in range(n+1)]
a, b = map(int, input().split())
m = int(input())
result = [0 for i in range(n+1)]            #[0, 2, 1, 0, 0, 0, 0, 0, 2, 2]


def bfs(start):
    q = deque()
    q.append(start)                         #   [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
    visit = [0 for i in range(n+1)]        #  [0, 1, 1, 0, 0, 0, 0, 1, 1, 1]
    visit[start] = 1                        #   q = [1, 7, 8, 9]
    while q:
        d = q.popleft()
        for i in chon[d]:
            if visit[i]==0:
                visit[i] = 1
                result[i] = result[d]+1
                q.append(i)

for _ in range(m):
    x, y = map(int, input().split())
    chon[x].append(y)
    chon[y].append(x)

bfs(a)
if result[b] ==0:
    result[b] = -1

print(result[b])
