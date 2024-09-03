import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    p1, p2 = 0, 0
    for i in range(n):
        a, b = map(str, input().split())
        if a == b:
            continue
        elif a == 'R':
            if b == 'P':
                p2 += 1
            elif b == 'S':
                p1 += 1
        elif a == 'P':
            if b == 'R':
                p1 += 1
            elif b == 'S':
                p2 += 1
        elif a == 'S':
            if b == 'R':
                p2 += 1
            elif b == 'P':
                p1 += 1
    if p1 > p2:
        print('Player 1')
    elif p1 < p2:
        print('Player 2')
    else:
        print('TIE')