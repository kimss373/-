z=[]
a=[]
for i in range(4):
    x, y = map(int, input().split())
    z.append(-x)
    z.append(y)
    a.append(sum(z))
a.sort()
print(a[-1])