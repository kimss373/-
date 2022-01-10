import sys
n=int(input())
a=[0]*10000
for i in range(n):
    b=int(sys.stdin.readline())
    a[b-1] = a[b-1] +1

for j in range(10000):
    if a[j]!=0:
        for k in range(a[j]):
            print(j+1)
