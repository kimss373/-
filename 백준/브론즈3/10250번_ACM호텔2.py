t=int(input())
k=[]
for i in range(t):
    h, w, n = map(int, input().split())
    for j in range(1, w+1):
        for l in range(1, h+1):
            if j>=10:
                k.append(str(l)+str(j))
            else:
                k.append(str(l)+"0"+str(j))
    print(k[n-1])
    k.clear()