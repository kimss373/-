t = int(input())
for _ in range(t):
    a = [1, 2, 4]
    n = int(input())
    for i in range(3, n):
        a.append(a[i-3] + a[i-2] + a[i-1])
    print(a[n-1])