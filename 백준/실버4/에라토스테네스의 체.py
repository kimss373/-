n, k = map(int, input().split())

arr = [i for i in range(2, n+1)]
now = arr[0]
idx = 0
count = 0
while True:
    if arr[idx] % now == 0:
        count += 1
        if count == k:
            print(arr.pop(idx))
            break
        else:
            arr.pop(idx)
            if idx == len(arr):
                now = arr[0]
                idx = 0
            continue
    idx += 1
    if idx == len(arr):
        now = arr[0]
        idx = 0
