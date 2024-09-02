arr = []
for i in range(9):
    arr.append(int(input()))

total = sum(arr)

idx1 = 0
idx2 = 1

while True:
    if total-arr[idx1]-arr[idx2] == 100:
        arr.pop(idx2)
        arr.pop(idx1)
        break

    idx2 += 1
    if idx2 == 9:
        idx1 += 1
        idx2 = idx1+1

arr.sort()
for i in range(7):
    print(arr[i])