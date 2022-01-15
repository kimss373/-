num = 1
while True:
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break
    else:
        if v % p >= l:
            print("Case {}:".format(num), (v // p) * l + l)
        else:
            print("Case {}:".format(num), (v // p) * l + v % p)
    num += 1