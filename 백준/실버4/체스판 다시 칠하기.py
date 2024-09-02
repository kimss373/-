n, m = map(int, input().split())

chess = []
bArr = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

wArr = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

for i in range(n):
    chess.append(input())

answer = 65
for i in range(0, n-7):
    for j in range(0, m-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(0, 8):
            for l in range(0, 8):
                if chess[i + k][j + l] != bArr[k][l]:
                    cnt1 += 1
                if chess[i + k][j + l] != wArr[k][l]:
                    cnt2 += 1
        if cnt1 < answer:
            answer = cnt1
        if cnt2 < answer:
            answer = cnt2

print(answer)