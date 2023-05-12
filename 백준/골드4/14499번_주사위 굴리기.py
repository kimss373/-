n, m, x, y, k = map(int, input().split())

up = [0, 0, 0, 0]
side = [0, 0]

diceMap = []

for i in range(n):
    row = list(map(int, input().split()))
    diceMap.append(row)

command = list(map(int, input().split()))

nowX = x
nowY = y

for i in command:
    switch = False
    if i == 1 and nowY + 1 < m:
        switch = True
        tmp = up[0]
        up[0] = side[0]
        side[0] = up[2]
        up[2] = side[1]
        side[1] = tmp
        print(up[0])
        nowY += 1

    elif i == 2 and nowY - 1 >= 0:
        switch = True
        tmp = up[0]
        up[0] = side[1]
        side[1] = up[2]
        up[2] = side[0]
        side[0] = tmp
        print(up[0])
        nowY -= 1

    elif i == 3 and nowX - 1 >= 0:
        switch = True
        tmp = up[0]
        up[0] = up[3]
        up[3] = up[2]
        up[2] = up[1]
        up[1] = tmp
        print(up[0])
        nowX -= 1

    elif i == 4 and nowX + 1 < n:
        switch = True
        tmp = up[0]
        up[0] = up[1]
        up[1] = up[2]
        up[2] = up[3]
        up[3] = tmp
        print(up[0])
        nowX += 1

    if switch:
        if diceMap[nowX][nowY] == 0:
            diceMap[nowX][nowY] = up[2]
        else:
            up[2] = diceMap[nowX][nowY]
            diceMap[nowX][nowY] = 0


