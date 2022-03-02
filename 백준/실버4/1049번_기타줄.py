import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a=[]
for i in range(m):
    x = tuple(map(int, input().split()))
    a.append(x)

min_set = 1000
min_notset = 1000
for i in range(m):
    if a[i][0] < min_set:
        min_set = a[i][0]
    if a[i][1] < min_notset:
        min_notset = a[i][1]
if n%6 == 0:
    y = min((n//6)*min_set, n*min_notset)
else:
    y = min((n//6+1)*min_set, (n//6)*min_set+n%6*min_notset, n*min_notset)
print(y)