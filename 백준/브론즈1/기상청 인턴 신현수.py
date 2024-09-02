n, k = map(int, input().split())

arr = list(map(int, input().split()))

now = sum(arr[:k])
max = now
for i in range(1, n-k+1):
    now = now - arr[i-1] + arr[i+k-1]
    if now > max:
        max = now

print(max)