n=int(input())
b=[]
for i in range(n):
    a=int(input())
    b.append(a)
b.sort()
for i in range(len(b)):
    print(b[i])