arr = list(map(int, input().split()))

start = min(arr)

while True:
    cnt = 0
    for i in range(5):
        if start % arr[i] == 0:
            cnt += 1
    if cnt > 2:
        break
    start += 1

print(start)
