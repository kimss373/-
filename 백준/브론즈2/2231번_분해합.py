n=int(input())
a=[]
b=[]
for i in range(1, n+1):
    a.append(str(i))
for j in range(n):
    c=0
    for k in range(len(a[j])):
        c += int(a[j][k])
    if int(a[j]) + c == n:
        if b ==[]:
            print(a[j])
            b.append(a[j])
        elif b!=[]:
            pass
if b==[]:
    print("0")