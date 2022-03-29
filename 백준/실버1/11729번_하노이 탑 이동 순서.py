n = int(input())

def hanoi(n, a, b, c):
    if n==1:
        move.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)
move = []
hanoi(n, 1, 2, 3)
print(len(move))
for i in range(len(move)):
    print(move[i][0], move[i][1])