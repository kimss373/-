t = int(input())
for i in range(t):
    a = tuple(input().split())
    for j in range(0, len(a), 1):
        for k in range(len(a[j])-1, -1, -1):
            print(a[j][k], end="")
        print(" ",end="")