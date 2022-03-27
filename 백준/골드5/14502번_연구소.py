import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
laboratory = []
for i in range(n):
    row = list(map(int, input().split()))
    laboratory.append(row)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0
virus_list = []
for i in range(n):
    for j in range(m):
        if laboratory[i][j] == 2:
            virus_list.append([i, j])

def select_wall(start, count):
    global result
    if count == 3:
        tmp_laboratory = copy.deepcopy(laboratory)
        for num in range(len(virus_list)):
            a, b = virus_list[num]
            speed_virus(a, b, tmp_laboratory)
        cnt = sum(i.count(0) for i in tmp_laboratory)
        result = max(result, cnt)
        return

    else:
        for i in range(start, n*m):
            a = i//m
            b = i%m
            if laboratory[a][b] == 0:
                laboratory[a][b] = 1
                select_wall(i, count+1)
                laboratory[a][b] = 0

def speed_virus(a, b, tmp_laboratory):
    if tmp_laboratory[a][b] == 2:
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0<= na < n and 0<= nb < m and tmp_laboratory[na][nb] == 0:
                tmp_laboratory[na][nb] = 2
                speed_virus(na, nb, tmp_laboratory)

select_wall(0, 0)
print(result)