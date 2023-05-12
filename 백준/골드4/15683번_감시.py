import copy
answer = 65
n, m = map(int, input().split())
cctv = [list(map(int, input().split())) for i in range(n)]

mode = [[],
        [[0], [1], [2], [3]],
        [[0, 1], [2, 3]],
        [[0, 2], [0, 3], [1, 2], [1, 3]],
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
        [[0, 1, 2, 3]]
        ]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

site = []
for i in range(n):
    for j in range(m):
        if cctv[i][j] != 0 and cctv[i][j] != 6:
            site.append([i, j, cctv[i][j]])

def fill(cctv, nm, x, y):
    for i in nm:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if cctv[nx][ny] == 6:
                break
            elif cctv[nx][ny] == 0:
                cctv[nx][ny] = '#'


def watch(cnt, arr):
    global answer

    if cnt == len(site):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        answer = min(count, answer)
        return

    temp = copy.deepcopy(arr)
    x, y, value = site[cnt]
    for i in mode[value]:
        fill(temp, i, x, y)
        watch(cnt + 1, temp)
        temp = copy.deepcopy(arr)

watch(0, cctv)
print(answer)

