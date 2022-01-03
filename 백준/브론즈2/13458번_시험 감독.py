import sys
n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
count = 0
for i in range(n):
    if a[i]-b < 0 :
        count = count + 1
    elif (a[i]-b)%c == 0:
        count = count + (a[i]-b)//c + 1
    else:
        count = count + (a[i]-b)//c + 2
print(count)