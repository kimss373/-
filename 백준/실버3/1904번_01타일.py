n = int(input())
a = {0:1, 1:2, 2:3, 3:5}
for i in range(4, n):
    a[i] = (a[i - 1] + a[i - 2])%15746

print(a[n-1])