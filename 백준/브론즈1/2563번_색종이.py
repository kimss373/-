n=int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x, x+10):
        for k in range(y, y+10):
            paper[k][j] = 1

count = 0
for row in paper:
    count += row.count(1)
print(count)