t=int(input())
for i in range(t):
    k = int(input()) #층
    n = int(input()) #호
    floor0=[]
    for j in range(1, n+1):
        floor0.append(j)

    for l in range(k):
        for p in range(1, n):
            floor0[p] += floor0[p-1]
    print(floor0[-1])