t = int(input())
for i in range(t):
    m, md, wd = map(int, input().split())
    row = 0
    total = 0
    for j in range(m):
        total += md
        if total % wd == 0:
            row -= 1
        if (total - md) % wd == 0:
            row -= 1
        row += (md // wd) + 2
    print("Case #", end="")
    print((i+1), end="")
    print(":", row)