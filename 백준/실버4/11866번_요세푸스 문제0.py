n, k = map(int, input().split())
a=[]
for i in range(1, n+1):
   a.append(i)

arr = []
x=k-1
while len(a)>=1:
    if x >= len(a):
        x -= len(a)
    else:
        arr.append(a.pop(x))
        x += k-1
print("<", end="")
for j in range(n-1):
    print(arr[j], end=", ")
print(arr[-1], ">", sep="")