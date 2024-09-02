t = int(input())

for i in range(t):
    tmp = input()
    score = 0
    cnt = 0
    for j in tmp:
        if j == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)