n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]

print('<', end="")
while len(arr) > 1:
    for i in range(k-1):
        arr.append(arr.pop(0))
    print(arr.pop(0), end=", ")

print(arr.pop(0), end=">")
