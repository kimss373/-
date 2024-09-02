n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]

print('<', end="")

length = len(arr)
idx = k-1
for i in range(n-1):
    print(arr.pop(idx), end=", ")
    length -= 1
    idx += k-1
    if idx >= length:
        idx %= length

print(arr.pop(0), end=">")
