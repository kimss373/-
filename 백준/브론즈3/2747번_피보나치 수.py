n=int(input())

x=[0, 1]
for i in range(n-1):
    x.append(x[0]+x[1])
    x.pop(0)
print(x[1])