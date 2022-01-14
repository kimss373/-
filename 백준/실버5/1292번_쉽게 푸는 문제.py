a, b = map(int, input().split())
arr = []
i = 0
while i*(i-1)<=2000:
    i += 1
    for j in range(1, i+1):
        arr.append(i)

print(sum(arr[a-1:b]))