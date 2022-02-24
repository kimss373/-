m, n = map(int, input().split())
if m ==1:
    m=2

while 2<=m<=n:
    x = 0
    for i in range(2, int(m**0.5)+1):
        if m%i == 0:
            x = 1
            break

    if x == 0:
        print(m)
    m += 1