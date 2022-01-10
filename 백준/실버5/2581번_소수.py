m=int(input())
n=int(input())
b=[]
for j in range(m, n+1):
    b.append(j)
while m<=n :
    if m < 3:
        if 1 in b:
            b.remove(1)
        m += 1
    else:
        for i in range(2, m):
            if m%i != 0:
                continue
            elif m%i==0:
                b.remove(m)
                break
        m +=1
b.sort()
if b==[]:
    print(-1)
else:
    print(sum(b))
    print(b[0])