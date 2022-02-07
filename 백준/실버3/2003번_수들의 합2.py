import sys
input = sys.stdin.readline
n, m = map(int, input().split())

a = list(map(int, input().split()))

cnt=0
start = 0
end = 1

while end<=n:
    if sum(a[start:end]) == m:
        start += 1
        cnt += 1
    elif sum(a[start:end]) < m:
        end += 1
    else:
        start += 1
print(cnt)