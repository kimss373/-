a, b = map(str, input().split())
c=0
d=0
for i in range(3):
    c += int(a[i])*10**i
for j in range(3):
    d += int(b[j])*10**j
if c>d:
    print(c)
else:
    print(d)