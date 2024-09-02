n = int(input())

tmp = list(map(int, input().split()))

tmp.sort()

if len(tmp) == 1:
    print(tmp[0]**2)
else:
    print(tmp[0]*tmp[n-1])