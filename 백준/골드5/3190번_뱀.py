import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
game = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    game[x][y] = 1

game[1][1] = 2

l = int(input())
command = []
for _ in range(l):
    a, b = map(str, input().split())
    command.append((a, b))

time = 0
direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
d = 0

snake = [[1, 1]]
while True:
    time += 1
    dx, dy = direction[d]
    nx, ny = snake[-1][0]+dx, snake[-1][1]+dy

    if nx==0 or ny == 0 or nx>n or ny > n or game[nx][ny] == 2:
        break

    if game[nx][ny]==0:
        snake.append([nx, ny])
        a, b = snake.pop(0)
        game[nx][ny] = 2
        game[a][b] = 0
    else:
        snake.append([nx, ny])
        game[nx][ny] = 2

    if command and command[0][0] == str(time):
        a, b = command.pop(0)
        if b == "D":
            if d == 0:
                d = 1
            elif d==1:
                d=3
            elif d==2:
                d=0
            else:
                d=2

        elif b=="L":
            if d==0:
                d=2
            elif d==1:
                d=0
            elif d==2:
                d=3
            else:
                d=1

print(time)