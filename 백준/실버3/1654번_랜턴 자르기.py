k, n = map(int, input().split())

lans = []
for i in range(k):
    lans.append(int(input()))

start = 1
end = max(lans)

while start<=end:
    mid = (start+end)//2
    cnt = 0
    try:
        for i in lans:
            cnt += i//mid
            if cnt > n:
                break
    except ZeroDivisionError:
        pass
    if cnt >= n:
        start = mid +1
    elif cnt < n:
        end = mid-1

print(end)