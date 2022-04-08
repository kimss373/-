n, m = map(int, input().split())
r, c, d = map(int, input().split())

dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]
room = []
for _ in range(n):
    row = list(map(int, input().split()))
    room.append(row)

room[r][c] = 2
cnt = 1
bcnt = 0

while True:
    nx = r+dxy[d][0]
    ny = c+dxy[d][1]
    d += 1
    d = d % 4
    if room[nx][ny] == 0:
        room[nx][ny] = 2
        r = nx
        c = ny
        cnt += 1
        bcnt = 0

    else:
        bcnt+=1

    if bcnt==4:
        d+=1
        d=d%4
        nx = r + dxy[d][0]
        ny = c + dxy[d][1]
        if room[nx][ny] == 1:
            break
        r = nx
        c = ny
        d += 3
        d = d%4
        bcnt = 0

print(cnt)
