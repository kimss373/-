n = int(input())
arr = list(map(int, input().split()))

now = 0
maxCnt = 0
cnt = 0
for i in range(n):
    if arr[i] > now:
        now = arr[i]
        cnt = 0
    else:
        cnt += 1
        if cnt > maxCnt:
            maxCnt = cnt

print(maxCnt)