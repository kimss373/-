n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr = reversed(arr)

cnt = 0
for i in arr:
    cnt += k // i
    k %= i

print(cnt)