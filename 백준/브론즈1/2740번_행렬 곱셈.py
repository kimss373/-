n, m = map(int, input().split())
A=[]
B=[]
C=[]
for _ in range(n):
    A.append(list(map(int, input().split())))
nn, mm = map(int, input().split())
for _ in range(nn):
    B.append(list(map(int, input().split())))
for _ in range(n):
    d=[]
    for _ in range(mm):
        d.append(0)
    C.append(d)
for i in range(n):
    for j in range(mm):
        for k in range(m):
            C[i][j] += A[i][k]*B[k][j]
for q in C:
    for l in q:
        print(l, end=" ")
    print()