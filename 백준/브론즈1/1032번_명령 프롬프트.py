n = int(input())
a=[]
for i in range(n):
    a. append(input())
for j in range(len(a[0])):
    b=[]
    for k in range(n):
        if a[0][j]==a[k][j]:
            b.append(0)
        else:
            b.append(1)
    if 1 in b:
        print("?", end="")
    else:
        print(a[0][j], end="")