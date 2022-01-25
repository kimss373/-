n = int(input())
stairs = [0]
score = [0] * (n+1)
for _ in range(n):
    stairs.append(int(input()))
if n == 1:
    print(stairs[1])

elif n == 2:
    print(stairs[1]+stairs[2])
else:
    score[1] = stairs[1]
    score[2] = stairs[1] + stairs[2]
    score[3] = max(stairs[1], stairs[2]) + stairs[3]
    for i in range(4, n+1):
        score[i] = max(score[i-3] + stairs[i-1] + stairs[i], score[i-2] + stairs[i])
    print(score[n])