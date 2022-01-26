
t = int(input())

for i in range(t):
    p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    n = int(input())

    if n > 10:
        for _ in range(n-10):
            p.append(0)
        for j in range(11, n+1):
            p[j] = p[j-1] + p[j-5]
    print(p[n])