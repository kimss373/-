t = int(input())

for _ in range(t):
    n = int(input())
    a = [(1, 0), (0, 1)]
    for j in range(n-1):
        a.append(0)
    for i in range(2, n+1):
        a[i] = (a[i-1][0] + a[i-2][0], a[i-1][1] + a[i-2][1])

    print(a[n][0], a[n][1])