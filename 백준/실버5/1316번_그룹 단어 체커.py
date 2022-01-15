n=int(input())
count = 0
for j in range(n):
    b=[]
    a = input()
    e = set(a)
    b.append(a[0])
    if len(e) == 1:
        count += 1
        continue
    else:
        for i in range(len(a)):
            if i<len(a)-1:
                if a[i] != a[i+1]:
                    b.append(a[i+1])

    b.sort()
    d=0
    for k in range(len(b)-1):
        if b[k] == b[k+1]:
            pass
        else:
            d += 1
        if d == len(b)-1:
            count += 1
print(count)
