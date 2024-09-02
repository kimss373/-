n, r, c = map(int, input().split())

list = [[], [0, 2]]

cnt = 1
now = 8
while True:
    if cnt >= r:
        break
    for i in range(len(list[1])):
        list[1].append(list[1][i]+now)
        cnt += 1
    now *= 4

list[0].append(list[1][r])
list[0].append(list[1][r]+1)

cnt = 1
now = 4
while True:
    if cnt >= c:
        break
    for i in range(len(list[0])):
        list[0].append(list[0][i]+now)
        cnt += 1
    now *= 4

print(list[0][c])