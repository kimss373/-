a, b = map(int, input().split())

arr = []

idx = 1
while len(arr) < 1000:
    for i in range(idx):
        arr.append(idx)
    idx += 1

print(sum(arr[a-1:b]))