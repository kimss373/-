n=int(input())
c=[]
for _ in range(n):
    x, y = map(int, input().split())
    c.append((x, y))

d=[]
for i in range(n):
    score = 1
    for j in range(n):
        if c[i][0]<c[j][0] and c[i][1]<c[j][1]:
            score += 1
    d.append(score)
for k in d:
    print(k, end=" ")