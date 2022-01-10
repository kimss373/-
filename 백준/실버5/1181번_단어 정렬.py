n=int(input())
a=[]
for i in range(n):
    a.append(input())

b = list(set(a))
b.sort()
for j in range(1, 51):
    for k in range(len(b)):
        if len(b[k])==j:
            print(b[k])