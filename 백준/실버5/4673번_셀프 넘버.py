a=[]
for i in range(1, 10001):
    a.append(str(i))
c=[]
for j in range(10000):
    b = int(a[j])
    for l in range(len(a[j])):
        b += int(a[j][l])
    if str(b) in a:
        c.append(str(b))
for k in range(len(c)):
    if c[k] in a:
        a.remove(c[k])
for u in range(len(a)):
    print(a[u])