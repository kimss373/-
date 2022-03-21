import sys
input = sys.stdin.readline
min_value = sys.maxsize

n = int(input())
price = [list(map(int, input().split())) for _ in range(n)]


def dfs(start, next, cnt, visit):
    global min_value

    if len(visit) == n:
        if price[next][start] != 0:
            min_value = min(min_value, cnt + price[next][start])
        return

    for i in range(n):
        if price[next][i] != 0 and i not in visit and cnt<min_value:
            visit.append(i)
            dfs(start, i, cnt + price[next][i], visit)
            visit.pop()


for j in range(n):
    dfs(j, j, 0, [j])

print(min_value)