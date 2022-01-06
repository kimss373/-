m=int(input())
n=int(input())

a=[]
for i in range(1, int(n**(1/2))+1):
    if m<= i**2 <= n:
        a.append(i**2)
if a==[]:
    print(-1)
else:
    print(sum(a))
    print(a[0])