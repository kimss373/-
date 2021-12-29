n=int(input())

for i in range(0, n+1):
    if i==0:
        k=1
    else:
        k*=i
print(k)